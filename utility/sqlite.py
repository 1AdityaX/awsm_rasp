import sqlite3

class Sqlite:
    def __init__(self, database, table) -> None:
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        self.table = table
    
    def update_value(self, attribute_name, value, check_val):
        query = f'update {self.table} set {attribute_name} = "{value}" where id={check_val}'
        self.cursor.execute(query)
        self.conn.commit()
        return
    
    def insert_data(self, values):
        query = f'insert into {self.table} values({values[0]}, "{values[1]}", "{values[2]}", {values[3]})'
        self.cursor.execute(query)
        self.conn.commit()
        return
    
    def get_all(self):
        query = f'select * from {self.table}'
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data
    
    def get_attr(self, attr):
        query = f'select {attr} from {self.table}'
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return [data[i][0] for i in range(0, len(data))]

    def get_spec(self, attr, id):
        query = f'select * from {self.table} where {attr}={id}'
        self.cursor.execute(query)
        data = self.cursor.fetchone()
        return data