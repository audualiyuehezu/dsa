def search(arr,n,x):
    for i in range(0,n):
         if arr[i] == x:
            return i
    return -1
#This is the where the code start interpreting
if  __name__ == "__main__":
    arr = [2,4,6,1,7]
    n = len(arr)
    x = 4

    ans = search(arr, n, x)
    if ans == -1:
       print("The array index has not been found")
    else:
        print(f"The array index is found")