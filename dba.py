
import csv, sqlite3, time
import locale
import dbf
import os.path
import HTML



locale.setlocale(locale.LC_ALL, '')

class database():
    def __init__(self):
        # self.conn = sqlite3.connect( "trans.db", detect_types=sqlite3.PARSE_DECLTYPES )
        self.conn = sqlite3.connect( "trans.db")
        self.conn.text_factory = str  #bugger 8-bit bytestrings
        self.cur = self.conn.cursor()
        self.path = None
        #catalogo Table
        self.cur.execute('''CREATE TABLE IF NOT EXISTS catalogo (
            cuenta VARCHAR, 
            nombre VARCHAR, 
            nomidioma VARCHAR, 
            tipo VARCHAR, 
            edoact VARCHAR, 
            ctamayor VARCHAR, 
            ctaefec VARCHAR, 
            fecalta VARCHAR, 
            sistorig VARCHAR, 
            clase VARCHAR, 
            digagru VARCHAR, 
            ccosto VARCHAR)''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS balance (
            CUENTA VARCHAR, 
            EJE INT, 
            TIPO INT, 
            SALDOINI INT, 
            IMP1 INT, 
            IMP2 INT, 
            IMP3 INT, 
            IMP4 INT, 
            IMP5 INT, 
            IMP6 INT, 
            IMP7 INT, 
            IMP8 INT, 
            IMP9 INT, 
            IMP10 INT, 
            IMP11 INT, 
            IMP12 INT, 
            IMP13 INT, 
            IMP14 INT, 
            CAPTADO BOOLEAN)''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS registros (
            EJE INT, 
            PERIODO INT, 
            TIPOPOL INT, 
            NUMPOL INT, 
            MOVTO INT, 
            CUENTA VARCHAR, 
            TIPOMOV BOOLEAN, 
            REFERENCIA VARCHAR, 
            IMPORTE FLOAT, 
            DIARIO INT, 
            MONEDA INT, 
            CONCEPTO INT, 
            FECHA DATE, 
            NUMPROV INT)''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS tipomov (
            NUMERO INT, 
            DESCRIP VARCHAR, 
            TIPO INT, 
            ULTPOL INT, 
            RNGINIPOL VARCHAR, 
            RNGFINPOL VARCHAR )''')

        self.conn.commit()
        self.movs = {1:'Ingresos',
                2: 'Egresos',
                3: 'Diario'}

    def import_accounts(self, csvfile):
        csvData = csv.reader(open(csvfile, "rb"))
        self.cur.executemany('INSERT OR IGNORE INTO catalogo VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(csvData))
        self.conn.commit()

    def import_balance(self, csvfile):
        csvData = csv.reader(open('balance.csv'))
        self.cur.executemany('INSERT OR IGNORE INTO balance VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(csvData))
        self.conn.commit()

    def import_records(self, csvfile):
        import datetime
        filetype = os.path.splitext(csvfile)[-1][1:].lower()

        if filetype == 'dbf':
            table = dbf.Table(csvfile)
            table.open()
            dbf.export(table, r'temp.csv', header =False)
            csvfile = 'temp.csv'
            
    
        elif filetype == 'csv':
            lines = open(csvfile, 'r').readlines()
            lines.pop(0)
            files = open(csvfile, 'w')
            for line in lines:
                files.write(line)
            files.close()

        csvData = csv.reader(open(csvfile, 'rb'))
        new_csv = []
        for line in csvData:
            L = line[:5] + [line[5].strip()] + line[6:]
            new_csv.append(L)

        self.cur.executemany('INSERT OR IGNORE INTO registros VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(new_csv))
        self.conn.commit()

        
    def import_relation(self, csvfile):
        csvData = csv.reader(open('relacion.csv'))
        self.cur.executemany('INSERT OR IGNORE INTO tipomov VALUES (?, ?, ?, ?, ?, ?)', tuple(csvData))
        self.conn.commit()        


    def get_records(self, start, end):
        # self.cur.execute('SELECT * from registros')
        self.cur.execute("""SELECT 
            cuenta,
            fecha,
            tipopol,
            numpol,
            referencia,
            tipomov,
            importe FROM registros WHERE cuenta >= ? AND cuenta <= ?  ORDER BY cuenta""", (start, end))
        return self.cur.fetchall()

    def get_accounts(self):
        return self.cur.execute("SELECT cuenta, nombre FROM catalogo").fetchall()

    def get_balance(self, start, end, month):
        endMonth = 'imp' + str(month)
        sqlstr = """SELECT balance.cuenta, balance.eje, %s, catalogo.nombre 
        FROM balance INNER JOIN catalogo ON balance.cuenta = catalogo.cuenta
        WHERE 
        balance.tipo = 1 
        AND (balance.cuenta >= %s AND balance.cuenta <= %s)
        ORDER BY balance.cuenta""" % (endMonth, start, end)
        self.cur.execute(sqlstr)
        return self.cur.fetchall()

    def print_aux(self, start, end, name, date):
        doc = open(os.path.join(self.path, 'documentos', name + '.html'), 'w')
        doc.write("""<style type="text/css">
                    <!--
                    @import url("style.css");
                    -->
                    </style>""")
        print date.Month, date.Year

        sep = [10, 10, 10, 20]

        saldo = 0
        cur_cta = ''
        acum = []
        for cuenta, fecha, tipopol, numpol, referencia, tipomov, importe in self.get_records(start, end):

            saldo += importe * (-1 if tipomov == 'True' else 1)
            fecha = fecha + " " * (sep[0] - len(fecha))
            tipopol = self.movs[tipopol] + " " * (sep[1] - len(self.movs[tipopol]))
            numpol = str(numpol) + " " * (sep[2] - len(str(numpol)))
            referencia = referencia + " " * (sep[3] - len(referencia))
            importe = (" " * (7 if tipomov == 'True' else 0)) + locale.currency(importe, grouping=True) + " " * (7 if tipomov == 'True' else 12)
            if cur_cta != cuenta:
                acum.append(['Saldo','','','','','', locale.currency(saldo, grouping=True)])
                acum.append(['','','','','','', ''])
                saldo = 0
                cur_cta = cuenta
            acum.append([cuenta, fecha, tipopol, numpol, referencia, importe, locale.currency(saldo, grouping=True)])

        htmlcode = HTML.table(acum, attribs={'id':"hor-minimalist-b"}, border=0,
                        header_row=['Cuenta', 'Fecha', 'Tipo', '#Poliza', 'Ref', 'Importe', 'Saldo'])

        doc.write(htmlcode)

    def print_sumaria(self, start, end, month, name=None):
        f = open(name+'.html', 'w')

        recordList = list(self.get_balance(start, end, month))
        cuentas = list(set([x[0] for x in recordList]))
        cuentas.sort()
        f.write("""<style type="text/css">
                    <!--
                    @import url("style.css");
                    -->
                    </style>""")
        sort_sum = []
        acum_ant = 0
        acum_cur = 0
        for i in cuentas:
            for j in recordList:
                if i == j[0] and j[1] == 2000:
                   #used to create the html file 
                   temp_l = [j[0], j[3], locale.currency(j[2], grouping=True)]
                   sal_ant = j[2]
                   acum_ant += j[2]
                   startString = j[0] + '\t' + j[3] 
                   startString+= " " * (50-len(startString)) + " " * (16 -len(locale.currency(j[2], grouping=True))) + locale.currency(j[2], grouping=True) + "   "

                elif i==j[0] and j[1] ==2001:
                    dif = j[2] - sal_ant
                    acum_cur += j[2]
                    perc = "{:.0f}%".format(float(j[2]) / (1 if sal_ant == 0 else float(sal_ant))*100) 
                    temp_l += [locale.currency(j[2], grouping=True), locale.currency(dif, grouping=True), perc]
                    sort_sum.append(temp_l)

        sort_sum.append(['Total', '', locale.currency(acum_ant, grouping=True), 
            locale.currency(acum_cur, grouping=True)])
        
        htmlcode = HTML.table(sort_sum, attribs={'id':"hor-minimalist-b"}, border=0,
                        header_row=['Cuenta', 'Nombre', 'Saldo 2000', 'Saldo 2001', 'Diferencia', '% de cambio'])
        f.write(htmlcode)


if __name__ == '__main__':
    d = database()
    # d.import_accounts('cuentas.txt')
    # d.import_records('CTW10004.DBF')
    # d.import_balance('balance.csv')
    # d.import_relation('relacion.csv')

    # d.print_aux('101000', '102000')
    d.print_sumaria('500000', '599999', 12, 'Sumaria de Efectivo')