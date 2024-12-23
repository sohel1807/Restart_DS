def bubblesort(arr):
    n=len(arr)

    for i in range(n):

        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

arr=[23,56,12,67,10]
print(bubblesort(arr))