'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    lower = 0
    upper = k
    maximum = []
    
    while upper <= len(nums):
        res = 0
        
        for count, i in enumerate(nums[lower:upper]):
            if count == 0:
                res = i
            elif i > res:
                res = i
                
        maximum.append(res)
        lower += 1
        upper += 1
    
    return maximum


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    # arr = [1, 3, -1, -3, 5, 3, 6, 7]
    arr = [1,3,-1,-3,5,3,6,7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
