import aleatorio as a
import media as m

lista = a.geraListaInteiro(10)

media = m.media(lista)
mediana = m.mediana(lista)
moda = m.moda(lista)

print("Minha lista:")
print (lista)
print (f"Media: {media}")
print (f"Mediana: {mediana}")
print (f"Moda: {moda}")