#!/usr/bin/env python3

""" DB Connector """

from request import RequestBuilderMySQL, RequestBuilderPostgreSQL 

class Connection:
    """Connect define a base connection for the other controller
    
    Controllers: MySQL, postgreSQL, Oracle, etc..

    """

    def __init__(self, host, db, user, passwd, builder):
        self.host = host
        self.db = db
        self.user = user
        self.passwd = passwd
        self.builder = builder
        self.connector = None

    def connect(self):
        pass

    def disconnect(self):
        pass

    def create(self, request):
        pass

    def read(self, request):
        pass

    def update(self, request):
        pass

    def delete(self, request):
        pass

class MySQLConnection(Connection):

    def __init__(self, host, db, user, passwd):
        super().__init__(host, db, user, passwd, RequestBuilderMySQL())

class PostgreSQLConnection(Connection):

    def __init__(self, host, db, user, passwd):
        super().__init__(host, db, user, passwd, RequestBuilderPostgreSQL())

if __name__ == "__main__":

    mysql = MySQLConnection("localhost", "thivolld", "thivolld", "thivolld")