#algorithm
#choose a pivot element and separate the numbers smaller to left and greater to right
#recursively sort the two sides 

#doing partition to figure out the pivot element
def partition(nums,start = 0,end = None):
    if end is None:
        end = len(nums) - 1
    l,r = start,end-1
    while(l<=r):
        if nums[l]<=nums[end]:
            l+=1
        elif nums[r] > nums[end]:
            r-=1
        else:
            nums[l],nums[r]=nums[r],nums[l]
    if nums[l] > nums[r]:
        nums[l],nums[end] = nums[end],nums[l]
        return l
    else:
        return end

print(partition([1,5,6,2,0,11,4]))





    
