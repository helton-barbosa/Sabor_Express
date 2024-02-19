import os


restaurantes = ['Hirayama', 'Boi na Brasa', 'Portal do Sul']


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
    print(f'{texto}\n')


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'\nRestaurante {nome_do_restaurante} cadastrado com sucesso!\n')
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

    for restaurante in restaurantes:
        print(f'. {restaurante}')

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
            print('Ativar restaurante')
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
