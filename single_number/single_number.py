'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    index = 0
    
    while index <= len(arr) - 1:
        
        count = 0
        
        for i in arr:
            if index == len(arr) - 1 and count == 1:
                return i

            elif arr[index] == i:
                count += 1
            index += 1


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")