# this file is for database functions

import mysql.connector

def run_query(query, params=None):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mosi_5180204453",
            database="web_project"
        )
        
        cursor = connection.cursor(dictionary=True)
        
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        rows = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        return rows
    except mysql.connector.Error as error:
        print(f"Error: {error}")
        return None

    finally:
        if connection.is_connected():
            connection.close()


def check_exist(user_name: str):
    result = run_query('select * from users where user_name = %s', (user_name,))
    return bool(result)


def insert_user(values: tuple):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mosi_5180204453",
            database="web_project"
        )
        
        query = "INSERT INTO users (user_name, password, is_manager) VALUES (%s, %s, %s)"
        
        cursor = connection.cursor()
        cursor.execute(query, values)
        
        connection.commit()
    except mysql.connector.Error as error:
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            return True


