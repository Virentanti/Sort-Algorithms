def selection_sort(arr):
    for i in  range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    print(arr)

arr=[5,4,10,6,3,2,7,8]
selection_sort(arr)
