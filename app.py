import os

def exibir_nome_do_programa():
    print('''     
    
████████████████████████████████████████████████████████████████████████
██▀▄─██▄─██─▄█─▄─▄─█─▄▄─███▄─▄▄─█▄─▄▄▀█▄─▄▄─█▄─▀█▀─▄█▄─▄█▄─██─▄█▄─▀█▀─▄█
██─▀─███─██─████─███─██─████─▄▄▄██─▄─▄██─▄█▀██─█▄█─███─███─██─███─█▄█─██
▀▄▄▀▄▄▀▀▄▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▀▀▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀  
''')

print('Auto Premium\n')

print('1. Cadastrar Novo Cliente')
print('2. Listar Todos os Clientes')
print('3. Ativar Serviço')
print('4. Sair\n')


opção_escolhida = int(input('Escolha uma opção: '))
# opção_escolhida = int(opção_escolhida)   

def cadastrar_clientes():
    print('Você escolheu cadrastrar clientes')

def listar_clientes():
    print('Você escolheu listar todos os clientes')

def ativar_servico():
    print('Você escolher mostrar sua publicação')   


def finalizar_programa():
    os.system('cls')
    print('finalizar o app\n')


if opção_escolhida == 1:
    print('Cadastrar Novo cliente')
elif opção_escolhida == 2:
    print('Listar Todos os clientes')
elif opção_escolhida == 3:
    print('Ativar Serviço')
else:
    print('finalizar programa')

def main():
    exibir_nome_do_programa()    

if __name__ == '__main__':
    main()
    