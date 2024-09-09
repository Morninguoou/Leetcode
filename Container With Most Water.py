class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # คำนวณความกว้างและความสูงของพื้นที่
            width = right - left
            height_val = min(height[left], height[right])
            area = width * height_val
            
            # เก็บค่าพื้นที่ที่มากที่สุดที่พบ
            max_area = max(max_area, area)
            
            # เลื่อน pointer ขึ้นอยู่กับความสูงของแท่ง
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
