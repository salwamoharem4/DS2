def _merge_sort(arr,l,h):
    if l>=h:
        return

    mid=(l+h)//2
    _merge_sort(arr,l,mid)
    _merge_sort(arr,mid+1,h)
    merge(arr,l,mid,h)


def merge(arr,l,mid,h):
    left=arr[l:mid+1] 
    right=arr[mid+1:h+1] #h+1 mesh maana fel interval

    i=j=0
    k=l
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1

def merge_sort(arr):
    _merge_sort(arr,0,len(arr)-1)
    return arr