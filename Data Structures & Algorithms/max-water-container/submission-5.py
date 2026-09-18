class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_val = r * min(heights[0], heights[-1])
        max_lh, max_rh = heights[0], heights[-1]
        while l < r:
            if max_lh < max_rh:
                l += 1
                if heights[l] > max_lh:
                    max_lh = heights[l]
                    max_val = max((r - l) * min(max_lh, max_rh), max_val)
            else:
                r -= 1
                if heights[r] > max_rh:
                    max_rh = heights[r]
                    max_val = max((r - l) * min(max_lh, max_rh), max_val)
        return max_val