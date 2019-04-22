import logging

logging.basicConfig(level=logging.DEBUG)  # basicConfig działa tylko przed pierwszym logowaniem

logging.debug('Najbardziej szczegółowy poziom.')
logging.info('Gdy aplikacja działa dobrze, informacyjnie.')
logging.warning('Wszystko działa, ale użytkownik musi być powiadomiony o czymś niepokojącym.')
logging.error('Program napotkał błąd uniemożliwiający poprawne działanie.')
logging.critical('Najpoważniejszy błąd, często oznajmiający zakończenie działania programu.')
