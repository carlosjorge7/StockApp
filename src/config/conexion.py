import pymysql

def conexionMySQL():
    conn = pymysql.connect(host = 'localhost', user = 'root', password = '', db = 'inventario')
    return conn