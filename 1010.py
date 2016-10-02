total = 0
for i in xrange(0,2):
	entrada = raw_input()
	numeros = entrada.split()
	codigo, quantidade, valor = numeros

	quantidade = int(quantidade)
	valor = float(valor)

	total = total + (quantidade * valor)

print "VALOR A PAGAR: R$ %.2f" % total