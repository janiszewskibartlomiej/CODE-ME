import log

log.basicConfig(filename='przyklad.log', level=log.DEBUG)

log.debug('Logujemy szczególiki')
log.info('Informuję, że to już drugi komunikat')
log.warning('Uwaga! Skrypt się kończy!')
