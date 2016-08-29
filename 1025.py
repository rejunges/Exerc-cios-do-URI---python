inputNQ = raw_input().split()
n = int(inputNQ[0])
q = int(inputNQ[1])
	
num_casos = 0
while n != 0 and q != 0:
	num_escritos = []
	consultas = []
	num_casos += 1
	
	#print n,q
	print "CASE# %d:" % (num_casos)
	
	for i in xrange(n):
		num_escritos.append(input())

	num_escritos.sort()
	dicionario = {}
	#Coloca os numeros num dicionario indicando quando aparecem a primeira vez, dessa forma a busca sera constante e nao linear
	for i in xrange(n):
		if num_escritos[i] in dicionario:
			continue
		dicionario[num_escritos[i]] = i

	#print dicionario

	for i in xrange(q):
		consultado = input()
		if consultado in dicionario:
			print "%d found at %d" % (consultado, dicionario[consultado] + 1)
		else:
			print consultado, "not found"

	inputNQ = raw_input().split()
	n = int(inputNQ[0])
	q = int(inputNQ[1])