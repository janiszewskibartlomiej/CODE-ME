import datetime

start = datetime.datetime.now()

import log

log.basicConfig(level=log.DEBUG)

czas_od_startu = datetime.datetime.now() - start

# stary sposób formatowania komunikatu
log.info('czas wykonania skryptu: %s ', czas_od_startu)

# można też bardziej współcześnie
log.info(f'czas wykonania skryptu: {czas_od_startu}')
