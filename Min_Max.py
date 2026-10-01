m=int(input("Enter the number of elements to be entered in an array: "))
arr=[]
for i in range(0,m):
    n=int(input("Enter the number: "))
    arr.append(n)
min=arr[0]
max=arr[0]
min2=arr[0]
max2=arr[0]
for j in arr:
    if(j<min):
        min2=min
        min=j
    elif j<min2 and j>min:
        min2=j
    elif min2==min and j>min:
        min2=j   
    if(j>max):
        max2=max
        max=j
    elif j>max2 and j<max:
        max2=j
    elif max2==max and j<max:
        max2=j
print("Largest is ",max)
print("Smallest is ",min)
print("2nd Largest is ",max2)
print("2nd Smallest is ",min2)
