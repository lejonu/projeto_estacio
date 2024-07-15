from typing import Any
from mysql import connector
# from dotenv import load_dotenv
import os
class DataBaseMeta(type):
  _instances = {}

  def __call__(cls, *args: Any, **kwds: Any) -> Any:
    if cls not in cls._instances:
      instance = super().__call__(*args, **kwds)
      cls._instances[cls] = instance
    return cls._instances[cls]

class DataBase(metaclass=DataBaseMeta):
  def __init__(self) -> None:
    self.url = os.getenv("host") 
    self.user = os.getenv("user")
    # connect
    self.connection = self.connect_to_db(os.getenv("password"))
    
  def connect_to_db(self, password):
    conn = None

    try:
      conn = connector.connect(
        host = self.url,
        user = self.user,
        passwd = password 
      )

      print(f"Connection to MySQL was successfull")
    except connector.Error as err:
      print(f"Error: {err}")

    return conn
  
  def create_db(self, database):
    cursor = self.connection.cursor()

    query = f"""
      CREATE DATABASE IF NOT EXISTS {database};
    """
      
    try:
      cursor.execute(query)
      print(f"Database {database} created sucessfully")
    except connector.Error as err:
      print(f"Error Creating DB: {err}")

  def execute_query(self, queryName, query):
    cursor = self.connection.cursor()

    try:
      cursor.execute(query)
      self.connection.commit()
      print(f"Query {queryName} has been executed successfully")
    except connector.Error as err:
      print(f"Error in Query: {err}")

  def fetch_data(self, query):
    cursor = self.connection.cursor()

    try:
      cursor.execute(query)
      result = cursor.fetchall()
      return result
    except connector.Error as err:
      print(f"Error: {err}")

  def execute_many_query(self, query, val):
    cursor = self.connection.cursor()

    try:
      cursor.executemany(query, val)
      self.connection.commit()
      print("Query for many executed")
    except connector.Error as err:
      print(f"Error: {err}") 
