from pathlib import Path
import sqlite3

class Banco_De_Dados():
    def __init__(self):
        BDE_DIR = Path(__file__).parent
        BDE_NAME = 'Estoque.sqlite3'
        BDE_FILE = BDE_DIR / BDE_NAME


        self.connection = sqlite3.connect(BDE_FILE)
        self.cursor = self.connection.cursor()
        self.TABLE_NAME = 'ESTOQUE'

        self.cursor.execute(
            f'create table if not exists {self.TABLE_NAME}'
            '('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'name text not null,'
            'price REAL not null ,'
            'amount integer not null,'
            'code integer unique not null '
            ')'
        )
        self.connection.commit()