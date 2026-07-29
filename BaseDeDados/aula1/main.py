import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
TABLE_NAME = 'customers'

# Danger: fazendo delete sem where MUITO CUIDADO
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
#DELETE mais CUIDADOSO
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



if __name__ == '__main__':
    print(sql)
    # DELETA COISAS DANGER
    cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id = 3')
    cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id = 1')
    
    #UPDATE ATUALIZA COISAS
    cursor.execute(f'UPDATE {TABLE_NAME} '
                   'SET name="QUALQUER", weight=8  WHERE id = 2')

    connection.commit()
    cursor.execute(f'SELECT * FROM {TABLE_NAME}')
    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    connection.close()