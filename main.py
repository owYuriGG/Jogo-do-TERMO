import menu_module
import game

def main():
    for _ in range(1):
        opc = menu_module.menu('')
        if opc == 1:
            game.play()
        elif opc == 2:
            file = open('used_words.txt', 'w')
            file.close()
        elif opc == 3:
            break

main()
