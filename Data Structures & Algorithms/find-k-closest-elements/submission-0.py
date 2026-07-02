class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    # find constrain conditions for what it means to be close
        idx = 0
        for i in range(1, len(arr)):
            if abs(x - arr[idx]) > abs(x - arr[i]):
                idx = i

        output = [arr[idx]]
        left = idx - 1
        right = idx + 1

        while len(output) < k:
            if left >= 0 and right < len(arr):
                if abs(x - arr[left]) <= abs(x - arr[right]):
                    output.append(arr[left])
                    left -= 1
                else:
                    output.append(arr[right])
                    right += 1
            elif left >= 0:
                output.append(arr[left])
                left -= 1
            elif right < len(arr):
                output.append(arr[right])
                right += 1
        return sorted(output)
        
