from selection import selection_sort
from merge import merge
#bastakhdem merge sort aady bas lama el section yewsal lel threshold bawaaf w bastakhdem el selection


def _hybrid_merge_sort(arr, l, h, threshold):
    if l >= h: #fi element wahed bas
        return

    if h - l + 1 <= threshold: #ba-calculate aadad el elements fi el section
        arr[l:h+1] = selection_sort(arr[l:h+1])
        return

    mid = (l + h) // 2

    _hybrid_merge_sort(arr, l, mid, threshold)
    _hybrid_merge_sort(arr, mid + 1, h, threshold)

    merge(arr, l, mid, h)


def hybrid_merge_sort(arr, threshold):
    _hybrid_merge_sort(arr, 0, len(arr) - 1, threshold)
    return arr