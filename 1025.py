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
	
	for i in xrange(0,n):
		#num_escritos.append(raw_input())
		num_escritos.append(input())

	num_escritos.sort()

	#removemendo repetidos
	"""for num in num_escritos:
		while num_escritos.count(num) > 1:
			num_escritos.remove(num)"""

	#consultas = raw_input()

	for i in xrange(0,q):
		#consultado = raw_input()
		consultado = raw_input()
		consultado = int(consultado)
		if(num_escritos.count(consultado)):
			print "%d found at %d" % (consultado, num_escritos.index(consultado) + 1)
		else:
			print str(consultado) + " not found"


	try:
		inputNQ = raw_input().split()
		n = int(inputNQ[0])
		q = int(inputNQ[1])
		
  	except (EOFError):	
  		break