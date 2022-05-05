
#for a list sorted in ascending order

def binary_search(nums,target):
    l = 0
    h = len(nums)-1
    while(l<=h):
        mid = l+(h-l)//2
        m = nums[mid]
        if m == target:
            return mid
        elif m<target:
            l = mid+1
        else:
            h = mid -1
    return -1

nums = [1,2,3,4,5,6]
target = 34
print(binary_search(nums,target))

