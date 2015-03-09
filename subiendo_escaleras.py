import random
result = list(xrange(1))
L = random.randint(1, 10000)
A = list(xrange(1))
B = list(xrange(1))
C = list(xrange(1))
#L = 20
def fibo(n):
	if n <= 1: 	
		return n
	else:
		return(fibo(n-1) + fibo(n-2))

N = 13
N2 = 15


print "existen",fibo(N+1),"maneras diferentes de subir una escalera de",N,"escalones"
print "existen",fibo(N2+1),"maneras diferentes de subir una escalera de",N2,"escalones"



for i in range(L):
	f = random.randint(1, L)
	g = random.randint(1, 20)
	A.insert(len(A), f)
	B.insert(len(B), g)
del A[0]
del B[0]
#print A
#print B
def escaleras(h,w):
	for i in range(L):
		C.insert(len(C), (fibo(h[i]+1) % (2*w[i])))
	del C[0]
escaleras(A, B)
print C
