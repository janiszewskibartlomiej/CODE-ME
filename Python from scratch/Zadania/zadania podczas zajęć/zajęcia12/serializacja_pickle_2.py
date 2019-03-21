import pickle

pickle_jimi = b'\x80\x03cdatetime\ndatetime\nq\x00C\n\x07\xb1\x08\x12\t\x00\x00\x00\x00\x00q\x01\x85q\x02Rq\x03.'

print(pickle_jimi)
print(type(pickle_jimi))

jimi = pickle.loads(pickle_jimi)

print(jimi)
print(type(jimi))
print('Rok koncertu:', jimi.year)

