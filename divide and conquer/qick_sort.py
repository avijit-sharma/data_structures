#algorithm
#choose a pivot element and separate the numbers smaller to left and greater to right
#recursively sort the two sides 

#doing partition to figure out the pivot element
def partition(nums,start = 0, end = None):
    if end is None:
        end = len(nums)-1
    l,r = start,end-1
    while(l<=r):
        if nums[l] <= nums[end]:
            l+=1
        elif nums[r] > nums[end]:
            r-=1
        else:
            nums[l],nums[r] = nums[r],nums[l]
    if nums[l] > nums[r]:
        nums[l],nums[end] = nums[end],nums[l]
        return l
    else:
        return end

def quicksort(nums, start=0, end=None):
    if end is None:
        nums = list(nums)
        end = len(nums) - 1
    
    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot-1)
        quicksort(nums, pivot+1, end)

    return nums

nums = [1,5,6,2,10,0,11,4]
print(partition([1,5,6,2,0,11,4]))
print(quicksort(nums))





    
