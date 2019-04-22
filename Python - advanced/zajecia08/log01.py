import logging

logging.debug('Najbardziej szczegółowy poziom.')
logging.info('Gdy aplikacja działa dobrze, informacyjnie.')
# dwa powyższe są wyciszone z założenia

# domyślny poziom logowania to WARNING
logging.warning('Wszystko działa, ale użytkownik musi być powiadomiony o czymś niepokojącym.')
logging.error('Program napotkał błąd uniemożliwiający poprawne działanie.')
logging.critical('Najpoważniejszy błąd, często oznajmiający zakończenie działania programu.')
