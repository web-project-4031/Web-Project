# this file is for database functions

import mysql.connector

def run_query(query, params=None):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mosi_5180204453",
            database="web_project"
        )
        
        cursor = conn.cursor(dictionary=True)
        
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        rows = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return rows
    except mysql.connector.Error as error:
        print(f"Error: {error}")
        return None

    finally:
        if conn.is_connected():
            conn.close()


def check_exist(user_name: str):
    result = run_query('select * from users where user_name = %s', (user_name,))
    return bool(result)
