#count_evens
def count_evens(nums):
    counter=0
    for x in range(len(nums)):
        if (nums[x]%2==0):
            counter+=1
    return counter

#big_diff
def big_diff(nums):
    largest=nums[0]
    smallest=nums[0]
    maxIndex = 0
    minIndex = 0
    for x in range(len(nums)):
        if(largest < nums[x]):
            maxIndex = x
            largest = nums[x]
        else
        if(smallest > nums[x]):
            minIndex = x
        smallest = min(nums[x], smallest)

#centered_average    
# def centered_average(nums):
#     largest=nums[0]
#     smallest=nums[0]
#     maxIndex = 0
#     minIndex = 0
#     
#     for x in range(len(nums)):
#         if(largest < nums[x]):
#             maxIndex = x
#             largest = nums[x]
#             maxCopies = []
#         elif(smallest > nums[x]):
#             minIndex = x
#             smallest = nums[x]
#             
#     