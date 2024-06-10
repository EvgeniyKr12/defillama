import pymysql
from .config import *


def get_update(table_name, url_id, column, content):
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
            sql_query = f"UPDATE {table_name} SET {column} = '{content}' WHERE url_id = '{url_id}'"

            cursor.execute(sql_query)
            connection.commit()
    finally:
        connection.close()

