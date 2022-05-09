#algorithm
#divide the list in equal parts 
#sort the smallest of unit and keep merging
#merge functiontakes two individually sorted lists and merge them together in a sorted way
def merge(nums1,nums2):
    merged = []
    i,j = 0,0
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<=nums2[j]:
            merged.append(nums1[i])
            i+=1
        else:
            merged.append(nums2[j])
            j+=1
    tail1 = nums1[i:]
    tail2 = nums2[j:]
    return merged+tail1+tail2
def mergesort(nums):
    if len(nums)<=1:
        return nums
    else:
        mid = len(nums)//2
        return merge(mergesort(nums[mid:]),mergesort(nums[:mid]))
num1 = [60,70,80,90]
num2 = [1,2,3,4,5]
num = merge(num1,num2)
print(mergesort([5, -12, 2, 6, 1, 23, 7, 7, -12]))