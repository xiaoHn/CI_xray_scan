# -*- coding: utf-8 -*-
import pymysql
class Database:
    hostname = '****'
    port = 33066
    user = 'root'
    password = '123456'
    db = 'vulscan'

    def __init__(self):
        self.connection = pymysql.Connect(host=self.hostname,port=self.port, user=self.user, passwd=self.password, db=self.db, charset='utf8')
        self.connection.ping(reconnect=True)
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except Exception, e:
            print e
            self.connection.rollback()

    def query(self, query):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)
        return cursor.fetchall()

    def __del__(self):
        self.connection.close()