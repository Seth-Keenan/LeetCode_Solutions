class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c and c == "(" or c == "[" or c == "{":
                stack.append(c)
            elif stack and c == ")" and stack[-1] == "(":
                stack.pop()
            elif stack and c == "]" and stack[-1] == "[":
                stack.pop()
            elif stack and c == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
        
        return len(stack) == 0
            

        
def testIsValid():

    s = "()"
    print(Solution.isValid(Solution, s))
    #Output: true

    s = "()[]{}"
    print(Solution.isValid(Solution, s))
    #Output: true

    s = "(]"
    print(Solution.isValid(Solution, s))
    #Output: false

testIsValid()