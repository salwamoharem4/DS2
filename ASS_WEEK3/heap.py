def heapify(arr,n,i): #ba-make sure en el subtree aand index i is a max heap
    largest=i   #o(logn)
    left= 2*i +1
    right= 2*i +2
    if left <n and arr[left]>arr[largest]:  #ba-check law el left child exists aslan w law akbar mn el largest
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    if largest !=i:  #law el largest etghayar ba-swap
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)

def build_heap(arr): #o(n)
    n=len(arr)
    #babdaa mn aand awel non-leaf node aashan el leaf nodes keda keda msh mehtageen heapify
    for i in range(n //2 -1,-1,-1): #mn akher parent node
        heapify(arr,n,i)

def heap_sort(arr): #o(nlogn)
    n=len(arr)
    build_heap(arr)
    for i in range(n-1,0,-1):  #bahot akbar element fi el akher
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)