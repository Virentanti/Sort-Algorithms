def bubble_sort(arr):
    n= len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
    print(arr)

#Driver Code
arr=[6,44,6,545,654,54,43]
bubble_sort(arr)
