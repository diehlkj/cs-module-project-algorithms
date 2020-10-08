'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here

    # print(n % 1)
    
    print(int(n / 2))
    print(n % 2)
    
    # print(n % 3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
