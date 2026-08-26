class Produto:
    def __init__(self, name, price, amount, code, id=None):
        self.id = id
        self.name = name
        self.price = price
        self.amount = amount
        self.code = code


class ProdutoRepository:
    def __init__(self, banco):
        self.banco = banco

    def salvar(self, produto):
        sql = (
            '''
            insert into estoque (name, price, amount, code)
            values (?, ?, ?, ?)
            ''')
        self.banco.cursor.execute(
            sql, 
            (
                produto.name,
                produto.price,
                produto.amount,
                produto.code
            )
        )

        self.banco.connection.commit()

    def listar(self):
        Estoque_Produto = []
        self.banco.cursor.execute(
            f'''select * from {self.banco.TABLE_NAME}''')
        
        for row in self.banco.cursor.fetchall(): 
                id, name, price, amount, code = row
                produto = Produto(id=id, name=name, price=price, amount=amount, code=code)
                Estoque_Produto.append(produto)
        return Estoque_Produto

    def update(self, produto):
        update3=(
            f'''update {self.banco.TABLE_NAME} set 
            name = ?,
            price = ?,
            amount = ?,
            code = ?
            where id = ?
            ''')
        
        self.banco.cursor.execute(
            update3, 
            (
                produto.name,
                produto.price,
                produto.amount,
                produto.code,
                produto.id
            )
        )
        self.banco.connection.commit()
    def delete(self, id):
        delete3 = (f'delete from {self.banco.TABLE_NAME} where id = ? ')

        self.banco.cursor.execute(
            delete3, (id,)
        )

        self.banco.connection.commit()
