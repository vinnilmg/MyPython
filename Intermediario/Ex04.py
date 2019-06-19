def abreArquivo():
	nome = input("\nDigitar nome do arquivo: ")
	arquivo = open(nome) #por padrão é 'r'
	return arquivo

def lerArquivo(arquivo):
	linhas = arquivo.readlines()

	for linha in linhas:
		print (linha.strip()) #strip tira espaços em branco do começo e final

esc = 0

while esc != 3:
        print("1 - Abrir arquivo \n2 - Ler arquivo \n3 - Fechar programa")
        esc = int(input("Digite a opção: "))
    
        if esc == 1:
            arquivo = abreArquivo()
        elif esc ==2:
        	try:
        		lerArquivo(arquivo)
        	except:
        		 print("\nVc deve abrir um arquivo antes de tentar ler!\n")

