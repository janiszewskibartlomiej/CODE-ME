import argparse

parser = argparse.ArgumentParser(description='Prosty program do cyfrowych powitań.')
parser.add_argument('-i', '--imie', help='Imie witanej osoby')
parser.add_argument('-l', '--lang', choices=['PL', 'EN'], default='PL', help='Język powitania')
parser.add_argument('filename', nargs='?', help='Nazwa pliku, do jakiego będzie zapisane powitanie.')

args = parser.parse_args()

jezyk = args.lang

powitania = {'PL': 'Cześć', 'EN': 'Hello'}

if args.imie:
    powitanie = f'{powitania[jezyk]}, {args.imie}!'
else:
    powitanie = f'{powitania[jezyk]}!'

if args.filename:
    with open(args.filename, mode='w') as f:
        f.write(powitanie)

print(powitanie)

# uruchom za pomocą: 
# `python args03.py -i Benek -j EN`
# `python args03.py -j EN -i Benek`
# `python args03.py -j EN
