#  https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_result = 0
        i = 0
        j = len(height) - 1
        max_result = (j - i) * min(height[i], height[j])
        while i < j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            max_result = max(max_result, (j - i) * min(height[i], height[j]))
        return max_result