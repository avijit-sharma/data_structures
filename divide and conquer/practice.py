# def merge(left,right):
#     result = []
#     i,j = 0,0
#     while i<len(left) and j<len(right):
#         if left[i]<=right[j]:
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[j])
#             j+=1
#     return result+left[i:]+right[j:]
# left = [1,2,3]
# right = [0,3,4]
# print(merge(left,right))
# def merge_sort(nums):
#     if len(nums)<=1:
#         return nums
#     else:
#         mid = len(nums)//2
#         return merge(merge_sort(nums[:mid]),merge_sort(nums[mid:]))
# print(merge_sort([1,5,3,7,3,5,4,-1]))

def partition(nums,end = None):
    if end is None:
        end =len(nums)-1
    l,r = 0 ,end -1
    while(l<=r):
        if nums[l] <= nums[end]:
            l+=1
        elif nums[r] > nums[end]:
            r -=1
        else:
            nums[l],nums[r] = nums[r],nums[l]
        if nums[l]>nums[r]:
            nums[l],nums[end] = nums[end],nums[l]
            return l
        else:
            return nums[end]

def quick(nums,start=0,end = None):
    if end is None:
        start =0 
        end = len(nums)-1
    else:
        while(start <= end):
            partition = partition(nums)
            quick(nums,partition)
            quick(nums,0,)


        
        