arr=[2,3,4,5,1,7,4,1,5,6]

#two numbers added upto 10

arr.sort()

pointer_1=0
pointer_2=len(arr)-1

count=0
print(arr)

while pointer_1<pointer_2:
    sum=arr[pointer_1]+arr[pointer_2]

    if sum==10:
        pointer_1+=1
        pointer_2-=1
        count+=1

    if sum<10:
        pointer_1+=1
        
    if sum>10:
        pointer_2-=1

print(count)