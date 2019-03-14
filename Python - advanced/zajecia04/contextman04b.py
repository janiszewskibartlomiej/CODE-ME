class Kolor:
    bcolors = {
        'HEADER': '\033[95m',
        'OKBLUE': '\033[94m',
        'OKGREEN': '\033[92m',
        'WARNING': '\033[93m',
        'FAIL': '\033[91m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m'
    }

    def __init__(self, kolor='HEADER'):
        self.kolor = self.bcolors[kolor]

    def __enter__(self):
        print(self.kolor, end='')

    def __exit__(self, *args):
        print('\033[0m', end='')


if __name__ == '__main__':
    with Kolor('OKGREEN'):
        print('hej!')
    with Kolor('OKBLUE'):
        print('hej!')
    with Kolor('WARNING'):
        print('hej!')
    with Kolor('BOLD'):
        print('hej!')
    with Kolor('FAIL'):
        print('hej!')

    print('hej!')
