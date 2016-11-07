# -*-coding:utf-8-*-
import pymysql

host="localhost"
user="root"
passwd=""
port=3306
db="patentsviewdata"
try:
    conn=pymysql.Connect(host=host,user=user,passwd=passwd,port=port,db=db)

    cur=None
    if conn:
        cur=conn.cursor()
    print "connection database success"

    cur.execute("select * from application limit5;")
    result=cur.fetchone()
    while result:
        print result
        result=cur.fetchone()
except e:
    print "Connection mysql database error! The error is %s",e
