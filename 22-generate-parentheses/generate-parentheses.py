class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack=[]
        def generateParantheses(open, close): #backtracking function.. recursion
            print(f"got open as {open=}, {close=}, {stack=}")
        
            if open == close == n:
                result.append("".join(stack))

            if open < n:
                stack.append('(')
                generateParantheses(open + 1, close)
                stack.pop()

            if close < open:
                stack.append(')')
                generateParantheses(open, close + 1)
                stack.pop()

        
        generateParantheses(0, 0)
        return result