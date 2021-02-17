#step1 import mysqlconnector

import mysql.connector

#step2 estable a connection with mysql

db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    auth_plugin='mysql_native_password'

)

#step3 create cursor to transport data to mysql and python wise versa
cursor=db.cursor()
sql='select version()'
cursor.execute(sql)
data=cursor.fetchone()
print(data)
db.close()
