m=int(input("Enter the number of elements to be entered in an array: "))
sum=0
arr=[]
for i in range(0,m):
    n=int(input("Enter the number: "))
    arr.append(n)
num=int(input("Enter the number to search: "))
for j in arr:
    if j==num:
        print("Found at position: ",i+1)
