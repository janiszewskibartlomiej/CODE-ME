from urllib.request import urlopen
import json

with urlopen('https://worldcup.sfg.io/teams/') as response:
    odpowiedz_json = response.read()
    print(odpowiedz_json)
    print(type(odpowiedz_json))

    print('---')

    mecze = json.loads(odpowiedz_json)

    print(mecze)
    print(type(mecze))