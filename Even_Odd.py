m=int(input("Enter the number of elements to be entered in an array: "))
e=0
o=0
arr=[]
for i in range(0,m):
    n=int(input("Enter the number: "))
    arr.append(n)

for j in arr:
    if(j%2==0):
        e+=1
    else:
        o+=1
print("Even are ",e)
print("Odd are ",o)
