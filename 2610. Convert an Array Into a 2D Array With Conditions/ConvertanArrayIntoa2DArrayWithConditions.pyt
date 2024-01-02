class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        while len(nums) > 0:
            lis = list(OrderedDict.fromkeys(nums).keys())
            res.append(lis)
            result = [nums.remove(item) for item in lis if item in nums]
        return res
