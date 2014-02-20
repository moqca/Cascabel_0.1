import HTML
import sqlite3

HTML_out = 'header.html'
f = open(HTML_out, 'w')

conn = sqlite3.connect( "trans.db")
conn.text_factory = str  #bugger 8-bit bytestrings
cur = conn.cursor()


cur.execute('SELECT * FROM catalogo ORDER BY cuenta')



htmlcode = HTML.table(cur.fetchall(),
	header_row=cur.fetchone())

f.write(htmlcode)