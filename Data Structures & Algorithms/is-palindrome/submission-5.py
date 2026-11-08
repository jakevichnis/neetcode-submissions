class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        output = [x.lower() for x in s if x.isalnum() == True]
        output = "".join(output)
        print(output)
        left = 0
        right = len(output) - 1
        while left <= right:
            if output[left] == output[right]:
                if left == right:
                    return True
                left += 1
                right -= 1
            else:
                return False
        return True
            
        
