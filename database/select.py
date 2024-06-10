import pymysql
from .config import *


def get_data_in_db(table_name, parameter):
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

            get_query = f"SELECT {parameter} FROM {table_name};"
            cursor.execute(get_query)
            result = cursor.fetchall()

    finally:
        connection.close()

    return result