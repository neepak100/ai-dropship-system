import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        column_definitions = ', '.join(columns)
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            {column_definitions}
        )
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert(self, table_name, **kwargs):
        columns = ', '.join(kwargs.keys())
        placeholders = ', '.join(['?'] * len(kwargs))
        insert_query = f"""
        INSERT INTO {table_name} ({columns}) VALUES ({placeholders})
        """
        self.cursor.execute(insert_query, tuple(kwargs.values()))
        self.connection.commit()

    def fetch_all(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()  

# Example usage:
# db = Database('my_database.db')
# db.create_table('users', ['id INTEGER PRIMARY KEY', 'name TEXT', 'age INTEGER'])
# db.insert('users', name='Alice', age=30)
# print(db.fetch_all('users'))
# db.close()