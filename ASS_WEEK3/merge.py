def _merge_sort(arr,l,h):
    if l>=h: #law el array fadya aw feha element wahed
        return

    mid=(l+h)//2
    _merge_sort(arr,l,mid) #sort left half
    _merge_sort(arr,mid+1,h) #sort right half
    merge(arr,l,mid,h) #merge them


def merge(arr,l,mid,h): #betakhod 2 halves sorted w te-combine them in one sorted section
    left=arr[l:mid+1] 
    right=arr[mid+1:h+1] #h+1 mesh maana fel interval

    i=j=0 #i hay-point aala el current element in left w j hay-point aala el current element in right
    k=l #beyshawer aala el makan ely hahot fih el element fi el sorted array
    while i<len(left) and j<len(right): #lehad ma el yekoon fi elements fi el 2 arrays
        if left[i]<=right[j]: #el left asghar
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j] #el right asghar
            j+=1
        k+=1
    while i<len(left): #lessa fi elements fi el left bahotaha zy ma heya
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right): #lessa fi elements fi el right bahotaha zy ma heya
        arr[k]=right[j]
        j+=1
        k+=1

def merge_sort(arr):
    _merge_sort(arr,0,len(arr)-1)
    return arr