import sqlite3
from sqlite3 import Error
from urllib.request import pathname2url
import pathlib

def create_connection(db_file):
    conn = None

    try:
        dburi = 'file:{}?mode=rw'.format(pathname2url(db_file))
       
        conn = sqlite3.connect(dburi, uri=True)
        
    except sqlite3.OperationalError:
        print(f"Could not find database. Creating new database with filename {db_file}.")