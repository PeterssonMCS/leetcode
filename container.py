class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i = 0
        j = len(height)-1
        max_area = 0
        
        while i < j:
            max_area = max(max_area,min(height[i],height[j])*(j-i))
            if height[i] > height[j]:
                j = j - 1
            else:
                i = i + 1
  
        return max_area
