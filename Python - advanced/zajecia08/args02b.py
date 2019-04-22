import argparse

parser = argparse.ArgumentParser(description='Prosty program do cyfrowych powitań.')
parser.add_argument('-i', '--imie', help='Imie witanej osoby')

args = parser.parse_args()

if args.imie:
    powitanie = f'Cześć, {args.imie}!'
else:
    powitanie = 'Cześć!'

print(powitanie)

# uruchom za pomocą: 
# `python args02b.py -i Benek`
# `python args02b.py -imie Benek`
