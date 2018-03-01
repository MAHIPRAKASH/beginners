def sumOfAP( A, D,N) :
    sum = 0
    I= 0
    while I < N :
        sum = sum + A
        A = A + D
        I= I + 1
    return sum
     
# Driver function
N = 3
A= 1
D = 1
print (sumOfAP(A, D, N))
 
