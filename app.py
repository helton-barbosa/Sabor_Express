import os


restaurantes = [
        {'nome': 'Ichiban', 'categoria': 'Japonesa', 'ativo': False},
        {'nome': 'Boi na Brasa', 'categoria': 'Churrascaria', 'ativo': True},
        {'nome': 'Dom Vergílio', 'categoria': 'Pizzaria', 'ativo': False}
    ]


def exibir_nome_do_programa():
    print('＞ Ｓａｂｏｒ Ｅｘｐｒｅｓｓ ＜\n')


def exibir_opcoes():
    print('1. C̳a̳d̳a̳s̳t̳r̳a̳r̳ R̳e̳s̳t̳a̳u̳r̳a̳n̳t̳e̳')
    print('2. L̳i̳s̳t̳a̳r̳ R̳e̳s̳t̳a̳u̳r̳a̳n̳t̳e̳')
    print('3. A̳t̳i̳v̳a̳r̳ R̳e̳s̳t̳a̳u̳r̳a̳n̳t̳e̳')
    print('4. S̳a̳i̳r̳\n')


def finalizar_app():
    exibir_subtitulo('Finalizar app')


def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()


def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(f'{texto}')
    print(f'{linha}\n')


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria,
        'ativo': False
        }
    restaurantes.append(dados_do_restaurante)
    print(f'\nRestaurante {nome_do_restaurante} cadastrado com sucesso!\n')
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'.ljust(20)}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}')

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Restaurante alternar estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'Restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'Restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('Restaurante não encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
