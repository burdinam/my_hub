ex = {'short': 'dict', 'long': 'dictionary'}

for i in ex:
    print(i)

for i in ex:
    print(ex[i])

for i in ex:
    print(i, ex[i])

for i in ex.values():
    print(i)

for x, y in ex.items():
    print(x, y)

x = ex.get("short")
print(x)

ex['medium'] = "dictio"

print(ex)

ex_copy = ex.copy()
print(ex_copy)

ex_copy.clear()
print(ex_copy)

ex_copy = dict(name1= "1-1", name2="2-2")
print(ex_copy)