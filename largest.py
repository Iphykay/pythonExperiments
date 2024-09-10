a=5
b=3
x=20

def compr(n,m,k):
    if n>m :
        if n>k : return(n)
        else: return(k)
    else:
        if m>k : return(m)
        else: return(k)

y=compr(a,b,x)
print("So it works \n")
print("Largest is " + str(y))
