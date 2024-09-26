# Solution

# // Time Complexity :  O(N)
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Greedy Solution - Start by keeping the last point as goal, find the previous location from where we can reach that end
# and then change the goal to that new found location and continue till we reach index 0.
# 
# DFS with DP -> Perform DFS for each index, and use a set to keep track of already DFS performed index so that we can
# avoid processing those again

# BFS with memoization -> Similar to DFS with DP, only thing is work on each level first using a queue and keep track
# if indexs already pushed to queue using a set, so that if we are getting same indexs again then we donot have to process
# them again.
# https://www.youtube.com/watch?v=GiZevzA0Wn4

# Greedy Solution
def canJump(nums):
    n = len(nums)
    final = n-1
    if n == 1:
        return True
    
    idx = final - 1

    while idx>=0:
        val = final - idx
        
        if val<=nums[idx]:
            final = idx
        
        idx = idx - 1
    
    if final == 0:
        return True
    else:
        return False
            
        


    # DP in DFS
    # def recursive(self,index,nums,processed):
    #     if index in processed:
    #         return False

    #     if index == len(nums)-1:
    #         return True
    #     elif index >= len(nums):
    #         return False
        
    #     while nums[index] > 0:
    #         output = self.recursive(index+nums[index],nums,processed)
    #         if output == True:
    #             return True
    #         else:
    #             nums[index] = nums[index] - 1
        
    #     processed.add(index)
    #     return False

    # def canJump(self, nums: List[int]) -> bool:
    #     processed = set()
    #     return self.recursive(0,nums,processed)

    # BFS with memoization
    # def bfs(self,idx,queue,nums,processed):
    #     val = nums[idx]      
    #     n = len(nums)

    #     while val>0:
    #         newIdx = idx + val
    #         if newIdx == n-1:
    #             return True
    #         elif newIdx < n-1:
    #             if newIdx not in processed:
    #                 queue.append(newIdx)
    #                 processed.add(newIdx)
            
    #         val = val - 1

    # def canJump(self, nums: List[int]) -> bool:
    #     if len(nums) == 1:
    #         return True

    #     processed = set()
    #     queue = deque()
    #     queue.append(0)
    #     processed.add(0)

    #     while len(queue) > 0:
    #         idx = queue.pop()
    #         retVal = self.bfs(idx,queue,nums,processed)
    #         if retVal == True:
    #             return True
        
    #     return False


    # DFS
    # def recursive(self,index,nums):
    #     if index == len(nums)-1:
    #         return True
    #     elif index >= len(nums):
    #         return False
        
    #     while nums[index] > 0:
    #         output = self.recursive(index+nums[index],nums)
    #         if output == True:
    #             return True
    #         else:
    #             nums[index] = nums[index] - 1
        
    #     return False
    # def canJump(self, nums: List[int]) -> bool:
    #     return self.recursive(0,nums)

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(canJump(nums))