def fibo(l):
	for i in range(1,26):
		b=l[i]+l[i-1]
		l.insert(i+1,b)
	return l


l=[]
l.append(0)
l.append(1)
l=fibo(l)
print(l[25])
