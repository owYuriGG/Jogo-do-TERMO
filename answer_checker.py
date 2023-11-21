def check_answer(word, user_attempt):
    RESET = "\033[0m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"

    word_letters = []
    user_attempt_letters = []
    used_words = []

    for caractere in word:
        word_letters += str(caractere)

    for letter in user_attempt:
         user_attempt_letters += letter

    for i in range(5):
          if user_attempt_letters[i] == word_letters[i]:
                user_attempt_letters[i] = f'{GREEN}{user_attempt[i]}{RESET}'
                used_words.append(user_attempt_letters[i])

    for i2 in range(5):
         if user_attempt_letters[i2] in word_letters and user_attempt[i2] not in used_words:
            user_attempt_letters[i2] = f'{YELLOW}{user_attempt[i2]}{RESET}'
            used_words.append(user_attempt[i2])


    print(f'\n| {user_attempt_letters[0]} | {user_attempt_letters[1]} | {user_attempt_letters[2]} | {user_attempt_letters[3]} | {user_attempt_letters[4]} |\n')
