# Progrm for even/Odd

arr = map(int,input().split())
arr = list(arr)
print(arr)
count1=0
count2=0
for i in range(len(arr)):
    if(arr[i]%2==0):
        count1+=1
    else:
        count2+=1

print("Number of even No.",count1)
print("Number of Odd No.",count2)