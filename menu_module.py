import utilities

def menu(message):
    try:
        utilities.clear()
        print(message)
        print('---------- T E R M O ----------')
        print('1 - Jogar')
        print('2 - Resetar palavras já utilizadas')
        print('3 - Sair')
        print('---------- T E R M O ----------')
        print()
        opc = int(input("Selecione uma opção: "))

        assert opc == 1 or opc == 2 or opc == 3, 'Você deve selecionar uma opção válida!'

        return opc
    except AssertionError:
        opc = menu('[ERRO] Você deve selecionar uma opção válida!')
        return opc
    except TypeError:
        opc = menu('[ERRO] Você deve selecionar uma opção válida!')
        return opc
    except ValueError:
        opc = menu('[ERRO] Você deve selecionar uma opção válida!')
        return opc
    except BaseException as error:
        opc = menu(f'[ERRO] {error}')
        return opc