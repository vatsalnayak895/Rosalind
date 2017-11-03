a=input("enter 1st number")
b=input("enter 2nd number")
if a > 10000 or b >10000:
    print("incorrect input enter value less thann 10000")
res=0
def sum(s):
 for i in range(a,b+1):
    if i%2!=0:
	s= s+i
 return s


print(sum(res))
