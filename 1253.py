numCasos = input()
for i in xrange(0,numCasos):
	palavra = raw_input()
	deslocamento = input()
	texto = tuple(palavra)
	criptografia = ""

	for j in xrange(0, len(texto)):
		valorLetra = ord(texto[j]) - deslocamento 
		if valorLetra < 65:
			valorLetra = 90 - (65 - valorLetra) + 1
		criptografia = criptografia + str(chr(valorLetra))
		
	print criptografia