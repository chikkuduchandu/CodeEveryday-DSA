class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        stack.append(asteroids[-1])
        for i in range(len(asteroids)-2,-1,-1):
            if not stack:
                stack.append(asteroids[i])
            else:
                if stack[-1]>0 and asteroids[i]>0:
                    stack.append(asteroids[i])
                elif stack[-1]>0 and asteroids[i]<0:
                    stack.append(asteroids[i])
                elif stack[-1]<0 and asteroids[i]<0:
                    stack.append(asteroids[i])
                elif stack[-1]<0 and asteroids[i]>0:
                    if abs(stack[-1])==asteroids[i]:
                        stack.pop()
                        continue
                    while stack and stack[-1]<0 and (abs(stack[-1])<asteroids[i]):
                        stack.pop()
                    if stack:
                        if stack[-1]<0 and abs(stack[-1])==asteroids[i]:
                            stack.pop()
                        elif stack[-1]>0:
                            stack.append(asteroids[i])
                    else:
                        stack.append(asteroids[i])
        ans=[]
        while stack:
            ans.append(stack.pop())
        return ans 

        
