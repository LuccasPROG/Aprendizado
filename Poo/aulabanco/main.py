"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança) Feito
    Pessoa tem nome e idade (com getters)Feito
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca) Feito
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta Feito
    ContaCorrente deve ter um limite extra Feito
    Contas têm agência, número da conta e saldo Feito 
    Contas devem ter método para depósito Feito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e Feito
    polimorfismo - as subclasses que implementam o método sacar) Feito
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""