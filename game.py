import utilities
import answer_checker

def play():
    utilities.clear()
    max_user_attemps = 4
    current_attemps = 0

    used_words = []
    word = utilities.sort_word()
    user_attempt = ''

    while word != user_attempt:
        if current_attemps <= max_user_attemps:
            while current_attemps <= max_user_attemps:

                user_attempt = utilities.user_input(used_words)

                used_words += [user_attempt]
                current_attemps += 1

                answer_checker.check_answer(word, user_attempt)

                if user_attempt == word:
                    print('Parabéns! Você descobriu a palavra!')
                    file = open(r'Python\Lab02\Semana12\TrabalhoG2\used_words.txt', 'a')
                    file.write(str(f'{word}\n'))
                    file.close()
                    break
        else:
            print('Você não conseguiu descobrir a palavra! ')
            print(f'A palavra correta era: {word}')
            break
