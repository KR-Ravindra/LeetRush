class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {'}':'{',']':'[',')':'('}
        stack = []
        for char in s:
            if char in bracket_pairs:
                if stack and stack[-1] == bracket_pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
