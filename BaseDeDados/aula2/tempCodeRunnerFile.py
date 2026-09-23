    with connection.cursor() as cursor:
        
        sql = (f' select * from {TABLE_NAME} ')

        cursor.execute(sql)
        data5 = cursor.fetchall()

        for row in data5:
            print(row)

    connection.commit()
