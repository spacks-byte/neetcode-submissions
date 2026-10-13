class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(i, dfsNums: List[int], remaining):
            #print(i, dfsNums)
            if remaining == 0:
                result.append(list(dfsNums))
                return
            if i >= len(candidates) or remaining < 0:
                return
            
            dfsNums.append(candidates[i])
            dfs(i + 1, dfsNums, remaining - candidates[i])
            dfsNums.pop()

            next_idx = i + 1
            while next_idx < len(candidates) and candidates[next_idx] == candidates[i]:
                next_idx += 1

            dfs(next_idx, dfsNums, remaining)

        dfs(0, [], target)
        return [list(x) for x in result]