from panda import Panda

panda1 = Panda('1', 'bla1@mail.bg', 'female' )
panda2 = Panda('2', 'bla2@mail.bg', 'female' )
pand32 = Panda('3', 'bla3@mail.bg', 'female' )

pandas = {}
key = hash(panda1)
pandas.update({hash(panda1): 1})
pandas.update(dict(panda2=2))
pandas.update(dict(panda3=3))

print(pandas)

print(float("inf"))
diction = {'d': 1, 'e': 2, 's': 0, 'i': 10 }
bestkey = None
bestValue = float('inf')
for key in diction:
    if diction[key] < bestValue:
        bestValue = diction[key]
        bestkey = key
print(bestkey)
