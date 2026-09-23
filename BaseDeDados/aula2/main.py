import pymysql
import dotenv
import pymysql.cursors

import os
dotenv.load_dotenv()

TABLE_NAME = 'customers'
connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=pymysql.cursors.DictCursor,
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'create table if not exists {TABLE_NAME} ('
            'id int not null auto_increment, '
            'name varchar(100), '
            'age int, '
            'primary key (id)'
            ')'
        )
        #DANGER: CUIDADO ISSO APAGA TODO O BANCO DE DADOS
        cursor.execute(f'truncate table {TABLE_NAME}')
    connection.commit() #Não necessita para criar tabelas

# INICIO:

    # Inserindo  um valor usando placeholder e um iteravel 
    with connection.cursor() as cursor:
        sql = (f' insert into {TABLE_NAME} '
            '(name, age) '
            'values (%s, %s)'
        )
        dados = ('lucas', 20)
        cursor.execute(sql, dados)
        
    connection.commit()
    # Inserindo  um valor usando placeholder e um Dicionario 

    with connection.cursor() as cursor:
        sql = (f' insert into {TABLE_NAME} '
            '(name, age) '
            'values (%(name)s, %(age)s)'
        )
        dados2= {
            "name": 'lu',
            "age": 20
        }
        cursor.execute(sql,dados2)
        
    connection.commit()

    # Inserindo  um valor usando placeholder e um um tupla de dicionarios
    with connection.cursor() as cursor:
        sql = (f' insert into {TABLE_NAME} '
            '(name, age) '
            'values (%(name)s, %(age)s)'
        )
        dados2= (
            {"name": 'edna',"age": 18},
            {"name": 'suelen',"age": 35},
            {"name": 'edson',"age": 50},
            {"name": 'lucca',"age": 20},
            {"name": 'valentina',"age": 8}
        )
        cursor.executemany(sql,dados2)
        
    connection.commit()

    # Inserindo  um valor usando placeholder e um um tupla de tuplas
    
    with connection.cursor() as cursor:
        sql = (f' insert into {TABLE_NAME} '
            '(name, age) '
            'values (%s, %s)'
        )
        dados3= (
            ('rodrigo', 13),
            ('jeniffer', 14),
            ('taina', 18),
            ('ana', 45),
            ('baby', 81),
        )
        result = cursor.executemany(sql,dados3)
        # print(sql) # mostra o calculo geral
        # print(dados3) #mostra o que foi adicionado
        # print(result) # verifica quantos foram inseridos
        
    connection.commit()

    # Inserindo  um valor usando placeholder e um um tupla de tuplas
    

    # Lendo os valores com SELECT
    with connection.cursor() as cursor:
        cursor.execute(
            f'select id, name, age from {TABLE_NAME}'
        )
    #     for row in cursor.fetchall():
    #         id, name, age = row
    #         print(id, name, age)
        
    # Lendo os valores com SELECT e previnindo project inject
    
    with connection.cursor() as cursor:
        # menor_id = int(input('Digite o menor Id: '))
        # maior_id = int(input('Digite o maior Id: '))

        sql = (f' select * from {TABLE_NAME} where id between %s and %s')
        
        # cursor.execute(sql, (menor_id, maior_id))
        # print(cursor.mogrify(sql, (menor_id, maior_id)))
        # data5 = cursor.fetchall()

        # for row in data5:
        #     print(row)

    connection.commit()
        
    # Apagando valores com DELETE e where e placeholders
    
    with connection.cursor() as cursor:

        sql = (f'delete from {TABLE_NAME}  where id= %s')

        result = cursor.execute(sql, (2))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME}')

        # for row in cursor.fetchall():
        #     print(row)
        # print(f'foi modificado {result} Row')

    # Update valores com DELETE e where e placeholders
    
    with connection.cursor() as cursor:

        sql = (f'UPDATE {TABLE_NAME} set name=%s, age=%s where id= %s')

        result = cursor.execute(sql, ("escanor", 107, 4))

        cursor.execute(f'SELECT * FROM {TABLE_NAME}')

        print('FOR 1:')
        for row in cursor.fetchall():
            print(row)


        print()
        print('FOR 2:')
        cursor.scroll(0, 'absolute')
        for row in cursor.fetchall():
            print(row)
    connection.commit()


