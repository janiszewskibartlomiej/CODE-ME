import log

log.debug('Najbardziej szczegółowy poziom.')
log.info('Gdy aplikacja działa dobrze, informacyjnie.')
# dwa powyższe są wyciszone z założenia

# domyślny poziom logowania to WARNING
log.warning('Wszystko działa, ale użytkownik musi być powiadomiony o czymś niepokojącym.')
log.error('Program napotkał błąd uniemożliwiający poprawne działanie.')
log.critical('Najpoważniejszy błąd, często oznajmiający zakończenie działania programu.')
