casosTeste = input()
for i in xrange(0, casosTeste):
	frase = raw_input()
	frase = tuple(frase)
	fraseFinal = ""
	
	for j in xrange(len(frase)/2-1, -1, -1):
		fraseFinal = fraseFinal + frase[j]

	for j in xrange(len(frase)-1, len(frase)/2-1, -1):
		fraseFinal = fraseFinal + frase[j]

	print fraseFinal
