class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()

        def dfs(i, dfsNums: List[int], remaining):
            #print(i, dfsNums)
            if remaining == 0:
                result.add(tuple(sorted(dfsNums)))
            if i >= len(nums) or remaining < 0:
                return
            dfsNums.append(nums[i])
            dfs(i, dfsNums, remaining - nums[i])
            dfsNums.pop()
            dfs(i+1, dfsNums, remaining)

        dfs(0, [], target)
        return [list(x) for x in result]