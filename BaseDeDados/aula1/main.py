import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
TABLE_NAME = 'customers'

# Danger: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
#MUITO CUIDADO
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)


#Create table
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
#Danger; SQL ingection
connection.commit()
#Insert one value
# cursor.execute(
#     f'INSERT INTO {TABLE_NAME} (Name, WEIGHT) '
#     'VALUES (?, ?),'
# )
sql = (
    f'INSERT INTO {TABLE_NAME} (Name, WEIGHT) '
    'VALUES (:nome, :peso)'
)
# cursor.execute(sql, ['Lucas', 19])
# cursor.executemany(sql, [['Lucas', 19], ['carlos', 20]])
cursor.execute(sql, {'nome': 'sem nome', 'peso': 3})
cursor.executemany(sql, ({'nome': 'sem nome', 'peso': 2},
                        {'nome': 'carlos', 'peso': 7},
                        {'nome': 'lucas', 'peso': 6},
                        {'nome': 'valentina', 'peso': 5},
                        {'nome': 'edson', 'peso': 2},))
connection.commit()
#Insert all value
# cursor.execute('')

cursor.close()
connection.close()


if __name__ == '__main__':
    print(sql)