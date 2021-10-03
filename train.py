from os import close
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
import pymysql
def get_conn():
     return pymysql.connect(
          host='127.0.0.1',
          user='root',
          password='love520wenyu',
          database='sql_db',
          charset='utf8'
)
def query_data(sql):
       
    conn=get_conn()
    try:  
        cursor=conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        return cursor.fetchall()
    finally: conn.close()
def insert_or_update_data(sql):
    conn=get_conn()
    try:  
        cursor=conn.cursor()
        cursor.execute(sql)
        conn.commit()        
    finally: conn.close()

if __name__=='__main__':
    sql='select *from student'
    datas=query_data(sql)
    import pprint
    pprint.pprint(datas)


