# bubble sort algorithm in Python is also called Adjacent swap / adjacent pair sorting algorithm. It is a simple sorting algorithm that works by repeatedly stepping through the list to be sorted, comparing each pair of adjacent items and swapping them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which means the list is sorted.
nums=[64, 34, 25, 12, 22, 11, 90]
def bubble_sort(num):
    n=len(num)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
bubble_sort(nums)
print(nums)
            ##time complexity of bubble sort is O(n^2) in worst and average case, and O(n) in best case. The space complexity of bubble sort is O(1) because it only requires a constant amount of additional memory space for the temporary variable used for swapping. */
# for best case
def bubble_sortbest(num):
    n=len(num)
    is_swapped=False
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
                is_swapped=True
        if is_swapped==False:
            return
