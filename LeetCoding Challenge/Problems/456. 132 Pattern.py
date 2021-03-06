'''
132 Pattern
https://leetcode.com/problems/132-pattern/

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:

Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.

Example 2:

Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:

Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
'''

#**********************************
#*********** VERSION 1 ************
#**********************************

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        mins = [nums[0]]
        for i in range(1, len(nums)):
            mins.append(min(mins[i-1], nums[i]))
        k = len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > mins[i]:
                while k < len(nums) and nums[k] <= mins[i]:
                    k += 1
                if k < len(nums) and nums[k] < nums[i]:
                    return True
                k -= 1
                nums[k] = nums[i]
        return False

#**********************************
#*********** VERSION 2 ************
#**********************************

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        tmp = float("-inf")
        for num in nums[::-1]:
            if tmp > num:
                return True
            while stack and num > stack[-1]:
                tmp = stack.pop()
            stack.append(num)
        return False
