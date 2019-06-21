import matplotlib.pyplot as plt

x = [1,3,5,7,9]
y = [2,3,7,1,0]
z = [200,25,400,3300,100]

titulo = "Scatterplot: Gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, label = "Meus pontos", color= 'k', marker='.', s=z) 
plt.plot (x, y, color='#000000', linestyle = "--" )
plt.legend()
#plt.show()
plt.savefig("teste1.pdf") #salvar
plt.savefig("teste1.png", dpi=300) #salvar