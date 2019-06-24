#Crescimento da população brasileira 1980-2016
#DataSus
import matplotlib.pyplot as plt

dados = open("populacao-brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
	if i != 0:
		linha = dados[i].split(';')
		#print(linha)
		x.append(int(linha[0]))
		y.append(int(linha[1]))

#print(x)
#print (y)
plt.bar(x, y, color="#e4e4e4")
plt.plot(x, y, color="k", linestyle="--")
#plt.scatter(x,y, color='k')

plt.title("Crescimento da população brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")
#plt.show()
plt.savefig("populacao-brasileira.png", dpi=300)