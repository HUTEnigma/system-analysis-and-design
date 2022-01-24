import pymysql.cursors

def get_database_connection(dictionary = True):
    if dictionary == True:
        
        db = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='golestan',
        cursorclass=pymysql.cursors.DictCursor
        )
    else:
        db = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='golestan'
        )
    dbcursor = db.cursor()
    return dbcursor, db

