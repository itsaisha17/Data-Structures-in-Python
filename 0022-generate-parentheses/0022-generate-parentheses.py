class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        # openN = opening brackets used
        # closeN = closing brackets used

        def backtrack(openN, closeN, curr):

            # valid string found
            if len(curr) == 2 * n:
                ans.append(curr)
                return

            # add opening bracket
            if openN < n:
                backtrack(openN + 1,
                          closeN,
                          curr + "(")

            # add closing bracket
            # only if valid
            if closeN < openN:
                backtrack(openN,
                          closeN + 1,
                          curr + ")")

        backtrack(0, 0, "")

        return ans