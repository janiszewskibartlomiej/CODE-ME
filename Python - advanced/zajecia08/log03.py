import logging

logging.basicConfig(filename='przyklad.log', level=logging.DEBUG)

logging.debug('Logujemy szczególiki')
logging.info('Informuję, że to już drugi komunikat')
logging.warning('Uwaga! Skrypt się kończy!')
