class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()

        def dfs(i, dfsNums: List[int]):
            #print(i, dfsNums)
            total = sum(dfsNums)
            if total == target:
                result.add(tuple(sorted(dfsNums)))
            if i >= len(nums) or total > target:
                return
            dfs(i, dfsNums + [nums[i]])
            dfs(i+1, dfsNums)

        dfs(0, [])
        return [list(x) for x in result]