
seq = "ATTVS"

arquivo = open("ex03.txt", 'w')

arquivo.write(">seq \n")
arquivo.write(seq)
arquivo.close()
print("Acabou")