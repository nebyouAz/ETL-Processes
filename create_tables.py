import pyodbc
import os

from queries import create_table_queries, drop_table_queries
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def connect_database():
    server = os.getenv("SERVER")
    database = os.getenv("DATABASE")
    username = os.getenv("UID")
    password = os.getenv("PASSWORD")
    connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    conn = pyodbc.connect(connectionString) 
    cur = conn.cursor()   
    return cur, conn
                         
def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()
                         
def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()                        
def main():
    cur, conn = connect_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()    

if __name__ == "__main__":
    main()                        
                         