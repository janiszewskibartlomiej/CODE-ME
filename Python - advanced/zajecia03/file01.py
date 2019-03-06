f = open('zen.txt', mode='r')

print(next(f).encode())
print(next(f).encode())
print(next(f).encode())
print(list(f))

print(next(f))
