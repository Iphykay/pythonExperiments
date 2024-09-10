a=5
b=3
x=20
y=2
A=0

def sum(n, m):
    global x
    x=x+n+m
    return (x)

for i in range(3):
  if i == 3 : continue
  print(i)
  print("end of iteration\n")
if A!=None: y=int(sum(a,b))
print("So it works \n")
print("x is " + str(x) + " y is " + str(y))
