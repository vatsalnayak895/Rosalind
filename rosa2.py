strt="mPteroclesBw6l4gNSXV6weT3JfkRGTRwdShyhqsj3dRlWAcaudolineatusDNRAAPMQDIm19iZZwMaQWtnI5bYcil04Tbv4JzlalkSMRnfncZobM8NsezJlEBkSQDjaqySm0ncVDLffj7u6eXvp3kQIVeSEg5zg8rTxxpgWQe5hRYusEsfBuVgd8KO60XhxhGycYkK"
if len(strt)>200:
	print("error")

def raw(s):
	a=input("no1")
	b=input("no2")
	c=input("no3")
	d=input("no4")	
	res=strt[a:b+1]+" "+strt[c:d+1]
	print(res)

raw(strt)
