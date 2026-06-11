''' only '(', ')' and '*'

true if valid (can escape all parenthesis)

'*' can be both '(' or ')' or ''

1 <= s.length <= 100

when do we decide if '*' is "(, ), empty"?
    - 3 options at each *
        + try 3 options recursively? will have repeating subproblems
        but how do we keep track of whether we have solved the parenthesis
            ~ at the last char, we can run thru the entire path and see if its valid?
                O(n^2) with memoization
        
we only need to know how many opening parenthesis we need to close and will the stars be able to close them?
we prioritize closing real openings, so at ')' we will pop from opening stack. if there are none, we pop
from start stack. if both are non then we can return False

at the end, we go thru the star stack starting from the top (-1) element. we check if its index is > opening[-1]
if its not that means we have remaining opening that we cant close

keep doing until we have no openings left


 '''
class Solution:
    def checkValidString(self, s: str) -> bool:
        openings = []
        stars = []

        for i in range(0, len(s)):
            char = s[i]
            if char == '(':
                openings.append(i)
            if char == '*':
                stars.append(i)
            if char == ')':
                if len(openings) > 0:
                    openings.pop()
                elif len(stars) > 0:
                    stars.pop()
                else:
                    return False
        
        while openings:
            if len(stars) <= 0:
                return False
            i = stars.pop()
            if i > openings[-1]:
                openings.pop()
            else:
                return False
        return True
        
            