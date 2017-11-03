def sqr_hypo(a,b):
    if a > 1000:
        print("invalid number")
	return False
    elif b > 1000:
        print("invalid number") 
	return False
    else:
        b=a*a+b*b
	return b

a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
res=(sqr_hypo(a,b))
print(res)
