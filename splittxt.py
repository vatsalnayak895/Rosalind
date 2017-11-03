with open('speech(1).txt','r') as f:
	read=f.readlines()
p=list(map(str.lower,read))
#print(p)
#q=[i.split() for  i in p]
l=[]
s=[]
for i in p:
	q=i.split()
	s+=q
	#print(q)
#print(s)
s.insert(0," ")	
for i in range(1,len(s)):
	if i%8==0:
		l.append(s[i])
l=list(map(str.upper,l))
#print(l)
a=0
for i in range(1,len(s)):
	if i%8==0:
#q.pop(i)
		s[i]=l[a]
		a+=1
	else:
		pass
print(*s)
















