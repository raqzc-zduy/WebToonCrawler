import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1111', db='moatoon', charset='utf8')

curs = conn.cursor()


sql = "insert into mo(id) value('g')"

curs.execute(sql)

sql = 'select * from mo'

curs.execute(sql)
rows = curs.fetchall()
print(rows)

conn.close()