import json
from sklep import warzywa_i_owoce

print(warzywa_i_owoce)

dane_json = json.dumps(warzywa_i_owoce)

print(dane_json)
print(type(dane_json))

decodowanie = json.loads(dane_json)

print (decodowanie)