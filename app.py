from time import sleep
import os

automoveis = [{'nome': 'Fusca', 'categoria': 'Hatch', 'ativo': True}, {'nome': 'Civic', 'categoria': 'Sedan', 'ativo': True}, {'nome': 'Fortuner', 'categoria': 'SUV', 'ativo': True}]

def nome_programa():
    print()
    print("""
    ████████████████████████████████████████████████████████████████████████
██▀▄─██▄─██─▄█─▄─▄─█─▄▄─███▄─▄▄─█▄─▄▄▀█▄─▄▄─█▄─▀█▀─▄█▄─▄█▄─██─▄█▄─▀█▀─▄█
██─▀─███─██─████─███─██─████─▄▄▄██─▄─▄██─▄█▀██─█▄█─███─███─██─███─█▄█─██
▀▄▄▀▄▄▀▀▄▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▀▀▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀ 
        """)

def exibir_opcoes():
    print('1. Cadastrar Automóvel')
    print('2. Listar Automóveis')
    print('3. Ativar/Desativar Automóvel')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app...')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * 70
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_automovel():
    exibir_subtitulo('Cadastro de novos Automóveis:')
    nome_automovel = input('Digite o nome do Automóvel que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do Automóvel {nome_automovel}: ')
    dados_automovel = {'nome': nome_automovel, 'categoria': categoria, 'ativo': False}
    print(f'O automóvel {nome_automovel} foi salvo com sucesso!')
    automoveis.append(dados_automovel)
    voltar_ao_menu_principal()

def listar_automoveis():
    exibir_subtitulo('Listando automóveis:')
    print(f'{"AUTOMÓVEL".ljust(22)} | {"CATEGORIA".ljust(20)} | STATUS')
    for automovel in automoveis:
        nome_automovel = automovel['nome']
        categoria = automovel['categoria']
        ativo = 'Ativado' if automovel['ativo'] else 'Desativado'
        print(f'- {nome_automovel.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alterar_situacao_automovel():
    exibir_subtitulo('Alterando estado do automóvel')
    nome_automovel = input('Digite o nome do Automóvel que deseja alterar o estado: ')
    automovel_encontrado = False
    for automovel in automoveis:
        if nome_automovel == automovel['nome']:
            automovel_encontrado = True
            automovel['ativo'] = not automovel['ativo']
            mensagem = f'O automóvel {nome_automovel} foi ativado com sucesso!' if automovel['ativo'] else f'O automóvel {nome_automovel} foi desativado com sucesso!'
            print(mensagem)
    if not automovel_encontrado:
        print('O automóvel não foi encontrado')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_automovel()
        elif opcao_escolhida == 2:
            listar_automoveis()
        elif opcao_escolhida == 3:
            alterar_situacao_automovel()
        elif opcao_escolhida == 4:
            finalizar_app()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
