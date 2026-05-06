class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]

        def backtrack(op,cl,curr):

            if len(curr)==2*n:
                ans.append(curr)
                return
            
            if op<n:
                backtrack(op+1,cl,curr+"(")
            
            if cl<op:
                backtrack(op,cl+1,curr+")")

        backtrack(0,0,"")
        return ans


        