
import random

def quick_sort(arr, low, high):
    if low < high:

        pi = randomized_partition(arr, low, high) #ba-return rl pivot's final position

        quick_sort(arr, low, pi - 1) #ba-sort el elements ely shemal el pivot

        quick_sort(arr, pi + 1, high) #ba-sort el elements ely yemeen el pivot


def randomized_partition(arr, low, high):

    random_index = random.randint(low, high) #bakhtar index random been el highw el low

    arr[random_index], arr[high] = arr[high], arr[random_index] #bahot el pivot fi el akher khales

    pivot = arr[high] #bakhaly el pivot akher element

    left = low
    right = high - 1

    while left <= right:

        while left <= right and arr[left] <= pivot: #bageeb awl element mn el shemal akbar mn el pivot
            left += 1

        while left <= right and arr[right] >= pivot: #bageeb awl element mn el yemeen asghar mn el pivot
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

    arr[left], arr[high] = arr[high], arr[left] #babadel el pivot ma3 el high(left)

    return left #ba-return el pivot's final index



