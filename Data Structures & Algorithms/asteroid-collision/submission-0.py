class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        # iterate through each asteroid
        for i in asteroids:
            # if stack is empty or current is positive, push
            if not stack or i > 0:
                stack.append(i)
            # if current is negative check against top of stack    
            else:
                alive = True
                while alive and stack and i < 0 and stack[-1] > 0:
                    # top explodes pop because its smaller
                    if abs(stack[-1] < abs(i)):
                        stack.pop()
            # if top positive, collision:
                    elif abs(stack[-1]) > abs(i):
                        alive = False
                
                    # top larger current explodes
                    else:
                        stack.pop()
                        alive = False
                if alive:
                    stack.append(i)

        return stack