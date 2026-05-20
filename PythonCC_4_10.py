#animales con características parecidas?
animales=["Perro","Gato","Hamster","Conejo","Gecko"]
#pues todos son domésticos de casa
for animal in animales:
    print("El "+animal+" sería una estupenda mascota.")
print("Al final todos son animales domésticos")

print("Primeros 3 elementos de la lista:")
primeros=animales[0:3]
for animal in primeros:
    print(animal)
print("En medio 3 elementos de la lista:")
enMedio=animales[1:4]
for animal in enMedio:
    print(animal)
print("Últimos 3 elementos de la lista:")
ultimos=animales[-3:]
for animal in ultimos:
    print(animal)
