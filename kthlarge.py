def kLargest(arr, k):
   
  arr.sort(reverse=True)
    
  for i in range(k):
     print (arr[i],end =" ") 


arr = [5,7,6,9,15,19]

k = 3
kLargest(arr, k)
