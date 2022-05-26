""" ------- Jump Game -------
You are given an integer array nums. 
You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
>>> Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. 
            Its maximum jump length is 0, which makes it impossible to reach the last index.
 """


""" -------- Approach 1: Backtracking -------- """
def canJump(nums):
    return canJump_from_position(0, nums)         

def canJump_from_position(position, nums):
    if position == len(nums) - 1:
        return True
    
    furthest_jump = min(position + nums[position], len(nums) - 1)

    # NOTE: checking next_position from right to left might make a small improve, though theoretical it is the same
    for next_position in range(furthest_jump, position, -1):
    # for next_position in range(position + 1, furthest_jump + 1):
        if canJump_from_position(next_position, nums):
            return True
    return False
    # Time: O(2 ^ N). There are 2^N (upper bound) ways to jump from the first position to the last,
    #                 where is the length of array `nums`
    # Space: O(N). Recursion needs additional memory for stack frames


""" -------- Approach 2: Dynamic Programming Top-down -------- """
# not as a class
memo = {}
def canJump(nums):
    for index in range(len(nums)):
        memo[index] = 'UNKNOWN'
    memo[len(nums) - 1] = 'GOOD'
    return canJump_from_position(0, nums)         

def canJump_from_position(position, nums):
    if memo[position] != 'UNKNOWN':
        return (memo[position] == 'GOOD')
    
    furthest_jump = min(position + nums[position], len(nums) - 1)

    for next_position in range(position + 1, furthest_jump + 1):
        if canJump_from_position(next_position, nums):
            memo[position] = 'GOOD'
            return True
    memo[position] = 'BAD'
    return False

print(canJump(nums=[2,3,1,1,4])) # expected output: True
print(canJump(nums=[3,2,1,0,4])) # expected output: False

# implemented as a class
class TopDownSolution:
    def __init__(self):
        self.memo = {}
        
    def canJump(self, nums):
        for index in range(len(nums)): 
            self.memo[index] = 'UNKNOWN'
        self.memo[len(nums) - 1] = 'GOOD'
        return self.canJump_from_position(0, nums)
    
    def canJump_from_position(self, position, nums):
        if self.memo[position] != 'UNKNOWN':
            return self.memo[position] == 'GOOD'
        
        furthest_jump = min(position + nums[position], len(nums) - 1)
        
        for next_position in range(position + 1, furthest_jump + 1):
            if self.canJump_from_position(next_position, nums):
                self.memo[position] = 'GOOD'
                return True
        self.memo[position] = 'BAD'
        return False
        # Time: O(n ^ 2) - For every element in the array, we are looking at the next elements to the right aiming to find a 'GOOD' index
        # Space: O(2N) = O(N) - For recursion and additional space needed to use memo table

# instance = TopDownSolution()
# result = instance.canJump([2,3,1,1,4]) 
# print(result) # expected output: True

# instance = TopDownSolution()
# result = instance.canJump([3,2,1,0,4]) 
# print(result) # expected output: False


""" -------- Approach 3: Dynamic Programming Bottom-up -------- """
# NOTE: This approach eliminates recursion
# NOTE: We only ever jump to the right; if we start from the right of the array, every time we will query a position to our right,
#       that position has already be determined as being GOOD or BAD, therefore removing the need for recursion as the we always hit the memo table

class BottomUpSolution:
    def __init__(self):
        self.memo = {}

    def canJump(self, nums):
        pass
class BottomUpSolution:    
    def canJump(self, nums):
        memo = {}
        for index in range(len(nums)):
            memo[index] = 'UNKNOWN'
        memo[len(memo) - 1] = 'GOOD'
        
        for position in range(len(nums) - 2, -1, -1):
            furthest_jump = min(position + nums[position], len(nums) - 1)
            
            for next_position in range(position + 1, furthest_jump + 1):
                if memo[next_position] == 'GOOD':
                    memo[position] = 'GOOD'
                    break
        return memo[0] == 'GOOD'
        # Time: O(n ^ 2) 
        # Space: O(n) for memo hash map

# bottom_up = BottomUpSolution()
# result = bottom_up.canJump([2,3,1,1,4])
# print(result) # expected output: True

# bottom_up = BottomUpSolution()
# result = bottom_up.canJump([3,2,1,0,4])
# print(result) # expected output: False

""" -------- Approach 4: Greedy -------- """
def canJump(nums):
    last_pos_good = len(nums) - 1

    for position in range(len(nums) - 1, -1, -1):
        if (position + nums[position]) >= last_pos_good:
            last_pos_good = position

    return last_pos_good == 0
    # Time: O(N) just a single pass through the `nums` array
    # Space: O(1)


result = canJump([2,3,1,1,4])
print(result) # expected output: True

result = canJump([3,2,1,0,4])
print(result) # expected output: False