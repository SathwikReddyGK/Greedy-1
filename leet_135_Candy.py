# Solution

# // Time Complexity :  O(N) -> O(2N)
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Forward flow to calculate the value based on left number
# Reverse flow to calculate the value based on right number
# https://www.youtube.com/watch?v=GiZevzA0Wn4

def candy(ratings):
    n = len(ratings)
    result = [1]*n
    for i in range(1,n):
        if ratings[i-1] < ratings[i]:
            result[i] = result[i-1] + 1
    
    sum = result[n-1]
    for i in range(n-2,-1,-1):
        if ratings[i+1] < ratings[i]:
            result[i] = max(result[i],result[i+1] + 1)
        
        sum += result[i]
            
    return sum

if __name__ == "__main__":
    ratings = [1,0,2]
    print(candy(ratings))