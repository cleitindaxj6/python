import os


automoveis = [
    {'nome': 'Modelo A', 'categoria': 'SUV', 'ativo': False},
    {'nome': 'Modelo B', 'categoria': 'Sedan', 'ativo': True},
    {'nome': 'Modelo C', 'categoria': 'Hatchback', 'ativo': False}
]

def exibir_nome_do_programa():
    
    print("""
        
████████████████████████████████████████████████████████████████████████
██▀▄─██▄─██─▄█─▄─▄─█─▄▄─███▄─▄▄─█▄─▄▄▀█▄─▄▄─█▄─▀█▀─▄█▄─▄█▄─██─▄█▄─▀█▀─▄█
██─▀─███─██─████─███─██─████─▄▄▄██─▄─▄██─▄█▀██─█▄█─███─███─██─███─█▄█─██
▀▄▄▀▄▄▀▀▄▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▀▀▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀  
""")

def exibir_opcoes():

    print("1. Cadastrar novo automóvel")
    print("2. Listar todos os automóveis")
    print("3. Alternar estado do automóvel")
    print("4. Sair\n")

def finalizar_app():

    exibir_subtitulo("Finalizar app")

def voltar_ao_menu_principal():
   
    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()

def opcao_invalida():
   
    print("Opção inválida\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_automovel():
   
    exibir_subtitulo("Cadastro de novos automóveis")
    nome_do_automovel = input("Digite o nome do automóvel que deseja cadastrar: ")
    categoria = input(f"Digite a categoria do automóvel {nome_do_automovel} (por exemplo, SUV, Sedan, Hatchback): ")
    dados_do_automovel = {'nome': nome_do_automovel, 'categoria': categoria, 'ativo': False}
    automoveis.append(dados_do_automovel)
    print(f"O automóvel {nome_do_automovel} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()

def listar_automoveis():

    exibir_subtitulo("Listando automóveis")
    print(f"{'Nome do Automóvel'.ljust(23)} | {'Categoria'.ljust(20)} | {'Status'}")
    for automovel in automoveis:
        nome_automovel = automovel['nome']
        categoria = automovel['categoria']
        ativo = "ativado" if automovel['ativo'] else "desativado"
        print(f" - {nome_automovel.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    voltar_ao_menu_principal()

def alterar_estado_automovel():
    
    exibir_subtitulo('Alterando estado do automóvel')
    nome_automovel = input("Digite o nome do automóvel que deseja alterar o estado: ")
    automovel_encontrado = False

    for automovel in automoveis:
        if nome_automovel == automovel['nome']:
            automovel_encontrado = True
            automovel['ativo'] = not automovel['ativo']
            mensagem = f"O automóvel {nome_automovel} foi ativado com sucesso" if automovel['ativo'] else f"O automóvel {nome_automovel} foi desativado com sucesso"
            print(mensagem)
            break

    if not automovel_encontrado:
        print("O automóvel não foi encontrado")

    voltar_ao_menu_principal()

def escolher_opcao():
 
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        if opcao_escolhida == 1:
            cadastrar_novo_automovel()
        elif opcao_escolhida == 2:
            listar_automoveis()
        elif opcao_escolhida == 3:
            alterar_estado_automovel()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
 
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
