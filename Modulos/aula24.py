from argparse import ArgumentParser

#Cria um objeto para a biblioteca
parser = ArgumentParser()

parser.add_argument('-b', '--basic', 
        help='Mostra olá Mundo na tela',
        type=str, #é o tipo 
        metavar='String', #Muda o nome tipo que aparece no --herp
        default='Ola Mundo ', #Mensagem Padrão
        required=False, #Obriga a Pessoa a Mandar o Comando
        # action='append',
        # nargs='+', #Recebe mais de um valor!
)       
parser.add_argument('-v', '--verbose', 
        help='Mostra logs',
        action='store_true'#mostra True or False
)       
args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de b')
    print(args.basic)
else:
    print('O valor de basic: ', args.basic)
    print(args.verbose)