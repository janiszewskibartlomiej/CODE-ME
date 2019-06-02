import log

log.basicConfig(level=log.DEBUG)  # basicConfig działa tylko przed pierwszym logowaniem

log.debug('Najbardziej szczegółowy poziom.')
log.info('Gdy aplikacja działa dobrze, informacyjnie.')
log.warning('Wszystko działa, ale użytkownik musi być powiadomiony o czymś niepokojącym.')
log.error('Program napotkał błąd uniemożliwiający poprawne działanie.')
log.critical('Najpoważniejszy błąd, często oznajmiający zakończenie działania programu.')
