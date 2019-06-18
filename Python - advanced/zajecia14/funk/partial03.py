import sys
from functools import partial

print('pierwszy', 'drugi', 'trzeci')
print('czwarty', 'piąty')

print2 = partial(print, sep='_', end=';')

print2('pierwszy', 'drugi', 'trzeci')
print2('czwarty', 'piąty')

# print2('a ten pójdzie do stderr', file=sys.stderr)
# print2('a ten pójdzie do pliku', file=open('partial03.out', mode='w'))
