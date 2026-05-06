class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        ans = [0] * n
        stack = []

        for curr in range(len(temperatures)):
            while stack and temperatures[curr] > temperatures[stack[-1]]:

                prev_index = stack.pop()

                ans[prev_index] = curr - prev_index  # days waited

            stack.append(curr)  # store
        return ans
