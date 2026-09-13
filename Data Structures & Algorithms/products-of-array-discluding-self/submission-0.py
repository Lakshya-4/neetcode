class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = 1
        for i in nums:
            res.append(pre)
            pre *= i
        pos = 1
        l = len(res) - 1
        for i in nums[::-1]:
            res[l] *= pos
            pos *= i
            l -= 1
        return res

