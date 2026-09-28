        cursor.execute(
            f'Select id from {TABLE_NAME} order by id desc limit 1'
        )