# Solution

# // Time Complexity :  O(N)
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Greedy Solution - Starting from index 0, check all the options you can jump to, to find the longest next jump. So at each
# level you are finding the longest next jump. Because, if you go to that index now, next jump will have more options and
# longer distance too
# 
# BFS with memoization and jump count - just keeping going to different levels and check if the reached level is the final
# level, keeping track of jumps/levels since we use memoization to avoid working on same options again is little tricky
# https://www.youtube.com/watch?v=0t474RdU7aY

from collections import deque
# Greedy
def jump(nums):
    queue = deque()
    queue.append(0)
    jumps = 0
    n = len(nums)
    
    if n == 1:
        return 0

    while len(queue) > 0:
        idx = queue.popleft()
        jumps += 1
        val = nums[idx]

        maxDist = 0
        while val>0:
            newIdx = val+idx
            if newIdx >= n-1:
                return jumps
            elif nums[newIdx]+newIdx >= n-1:
                return jumps+1
            if newIdx < n and maxDist < (nums[newIdx]+newIdx):
                maxDist = nums[newIdx]+newIdx
                if len(queue) > 0:
                    queue.pop()
                queue.append(newIdx)
            
            val -= 1

# BFS with memoization and jump count
# def bfs(idx,nums,curVal,jump,n,processed,queue):        
#     val = nums[idx]

#     while val>0:
#         newIdx = idx+val
#         if newIdx == n-1:
#             return curVal,jump
#         if newIdx not in processed:
#             queue.append(newIdx)
#             processed.add(newIdx)
#             curVal += 1
        
#         val = val-1
    
#     return curVal,None
    
# def jump(nums):
#     processed = set()
#     queue = deque()
#     queue.append(0)
#     jump = 1
#     preVal = 1
#     curVal = 0
#     n = len(nums)
#     jumpNum = None
#     processed.add(0)

#     if n == 1:
#         return 0

#     while len(queue) > 0:
#         idx = queue.popleft()
#         if preVal == 0:
#             jump += 1
#             preVal = curVal
#             curVal = 0
        
#         preVal -= 1
#         curVal,jumpNum = bfs(idx,nums,curVal,jump,n,processed,queue)

#         if jumpNum != None:
#             return jumpNum
    
if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(jump(nums))