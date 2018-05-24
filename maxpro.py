def multiply( array , n ):
    pro = 1
    for i in range(n):
        pro = pro * array[i]
    return pro
array = [1, 2, 3, 4, 5]
n = len(array)
print(multiply(array, n))
