import pymysql
from .config import *


def drop_data_mysql(table_name, column, data):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)
    except Exception as ex:
        print("Connection refused...")
        print(ex)
    try:
        cursor = connection.cursor()

        with connection.cursor() as cursor:
            table_name = table_name
            sql = f"DELETE FROM {table_name} WHERE {column} IN {tuple(data)}"
            cursor.execute(sql)

        connection.commit()
        print(f'Table "{table_name}" successfully dropped.')

    except Exception as ex:
        print("Connection refused...")
        print(ex)

