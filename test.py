import pymysql

connection = {
    'host': '',
    'username': 'mysqlAdmin',
    'password': '',
    'db': 'thisisatest'
}

con = pymysql.connect(
    host=connection['host'], user=connection['username'], password=connection['password'], database=connection['db'])

cursor = con.cursor()

print(cursor)
