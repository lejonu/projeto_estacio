from mysql import connector

class DataBase:
  def __init__(self, url, user, password) -> None:
    self.url = url 
    self.user = user
    # connect
    self.connection = self.connect_to_db(password)
    
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
