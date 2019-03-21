from urllib.request import urlopen
import json

with urlopen('https://yesno.wtf/api') as response:
    odpowiedz_json = response.read()
    # print(odpowiedz_json)
    # print(type(odpowiedz_json))

    # print('---')

    odpowiedz = json.loads(odpowiedz_json)

    # print(odpowiedz)
    # print(type(odpowiedz))

    print(odpowiedz['answer'])