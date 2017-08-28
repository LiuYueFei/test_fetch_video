import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="test", charset="utf8")
cur = conn.cursor()
cur.execute("USE test")
cur.execute("select * from t_college where id=1")
print(cur.fetchone())
cur.close()
conn.close()

