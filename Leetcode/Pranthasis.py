class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if(len(s)%2 != 0):
            print(False)

        else:
            stack1 = []
            x1  = '(' 
            x2  = ')'
            y1  = '['
            y2  = ']'
            z1  = '{'
            z2  = '}'


            for i in s:
                if(i == x1 or i == y1 or i == z1):
                    stack1.append(i)
                elif (len(stack1)==0):
                    return False
                elif(i == ')' and stack1[-1]=='('):
                    stack1.pop(-1)
                elif(i == ']' and stack1[-1]=='['):
                    stack1.pop(-1)
                elif(i == '}' and stack1[-1]=='{'):
                    stack1.pop(-1)
                else:
                    return False
            if (len(stack1) ==0):
                return True

        