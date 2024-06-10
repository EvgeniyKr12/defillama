import pymysql
from .config import *


def insert_data_mysql(table_name, data):
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
            insert_query = f"INSERT INTO {table_name} (data, value) VALUES{tuple(data)};"
            cursor.execute(insert_query)
            connection.commit()
    except Exception as ex:
        print("Connection refused...")
        print(ex)