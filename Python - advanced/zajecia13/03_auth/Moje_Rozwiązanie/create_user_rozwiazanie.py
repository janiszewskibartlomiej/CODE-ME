from werkzeug.security import generate_password_hash

if __name__ == '__main__':
    username = input('Podaj nazwę użytkownika: ')
    # username = 'testowy'

    password = input('Podaj hasło: ')
    # password = 'haslo'

    repetitions = 1  # spróbuj wygenerować kilka hashy

    for _ in range(repetitions):
        hashed_password = generate_password_hash(password)
        print(f'{password} -> {hashed_password}')
