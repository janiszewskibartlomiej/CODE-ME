import argparse

parser = argparse.ArgumentParser(description='Prosty program do cyfrowych powitań.')
parser.add_argument('-i', '--imie', nargs=2, help='Dokładnie dwa imiona witanych osoby')

args = parser.parse_args()

if args.imie:
    powitanie = f'Cześć, {args.imie}!'
else:
    powitanie = 'Cześć!'

print(powitanie)

# uruchom za pomocą: 
# `python args02c.py -i Benek Czesiek`
