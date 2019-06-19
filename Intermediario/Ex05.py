arquivo = open ('ex02.txt')

dic = {}
linhas = arquivo.readlines()


for linha in linhas:
	if '>' in linha:
		l = linha.strip()
		dic[l] = ""
	else:
		dic[l] = dic[l]+linha.strip()

print(dic.keys())
print(dic.values())
print(dic.items())
	

