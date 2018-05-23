
def largest(arr,n):
 
    max = arr[0]
 
    
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max
arr = [5,10,15,20,25]
n = len(arr)
Ans = largest(arr,n)
print ("maximum element",Ans)
