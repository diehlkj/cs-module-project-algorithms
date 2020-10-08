'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    occurrences = arr.count(0)
    
    if occurrences != 0 or occurrences != len(arr):
        position = 0
        
        while position < occurrences:
            try:
                arr.remove(0)
                arr.append(0)
                position += 1
            except ValueError:
                pass
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    # arr = [0, 0, 0, 0, 0, 1, 0]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")