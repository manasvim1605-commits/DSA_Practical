m=int(input("Enter the number of elements to be entered in an array: "))
sum=0
arr=[]
for i in range(0,m):
    n=int(input("Enter the number: "))
    arr.append(n)
    sum+=n
print("Sum is ",sum)