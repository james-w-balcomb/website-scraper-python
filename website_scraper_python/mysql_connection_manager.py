import pymysql


class MysqlConnectionManager(object):

    _instance = None
    mysql_connection = None
    mysql_cursor = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, host, port, user, passwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        if MysqlConnectionManager.mysql_connection is None:
            MysqlConnectionManager.mysql_connection = pymysql.connect(host = self.host,
                                                                      port = self.port,
                                                                      user = self.user,
                                                                      passwd = self.passwd,
                                                                      db = self.db)
            print('mysql_connection')
        if MysqlConnectionManager.mysql_cursor is None:
            MysqlConnectionManager.mysql_cursor = MysqlConnectionManager.mysql_connection.cursor()
            print('mysql_cursor')

    def __del__(self):
        MysqlConnectionManager.mysql_cursor.close()
        MysqlConnectionManager.mysql_connection.close()

    def __enter__(self):
        return self.mysql_connection

    def __exit__(self, *exc):
        MysqlConnectionManager.mysql_cursor.close()
        MysqlConnectionManager.mysql_connection.close()
