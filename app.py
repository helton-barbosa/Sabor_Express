import os


def exibir_nome_do_programa():
    print('＞ Ｓａｂｏｒ Ｅｘｐｒｅｓｓ ＜\n')


def exibir_opcoes():
    print('1. C̳a̳d̳a̳s̳t̳r̳a̳r̳ R̳e̳s̳t̳a̳u̳r̳a̳n̳t̳e̳')
    print('2. L̳i̳s̳t̳a̳r̳ R̳e̳s̳t̳a̳u̳r̳a̳n̳t̳e̳')
    print('3. A̳t̳i̳v̳a̳r̳ R̳e̳s̳t̳a̳u̳r̳a̳n̳t̳e̳')
    print('4. S̳a̳i̳r̳\n')


def finalizar_app():
    os.system('cls')


def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    print(f'Você escolheu a opção {opcao_escolhida}')

    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurante')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else:
        finalizar_app()


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
