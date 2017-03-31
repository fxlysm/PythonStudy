import pypyodbc
pypyodbc.win_create_mdb('D:\\salesdb.mdb')

# conn = pypyodbc.connect('Driver=MDBTools;DBQ=/root/Templates/qq/Data.mdb', unicode_results=False)
#
# print(conn.cursor().execute('select * from dm_mobile').fetchone()[2].decode('utf8'))

conn = pypyodbc.connect('Driver={Microsoft Access Driver (*.mdb)};DBQ=D:\\salesdb.mdb')
cur = conn.cursor()
cur.execute('''CREATE TABLE saleout (
ID COUNTER PRIMARY KEY,
customer_name VARCHAR(25),
product_name VARCHAR(30),
price float,
volume int,
sell_time datetime);''')
cur.commit()