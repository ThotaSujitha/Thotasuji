n=[]
length=int(input("Enter Length of List : "))
print("Enter List values")
for i in range(0,length):
    k=int(input("Enter list Element : "))
    n.append(k)
print("Before swap : \n",n)
n[length-1],n[0]=n[0],n[length-1]
print("After Swap : \n",n)
