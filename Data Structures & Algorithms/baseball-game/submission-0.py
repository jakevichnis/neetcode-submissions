class Solution:
    def calPoints(self, operations: List[str]) -> int:
        output = []
        for i in range(len(operations)):
            
            if operations[i] == "+":
                new_score = output[-2] + output[-1]
                output.append(new_score)
            elif operations[i] == "D":
                new_score = output[-1] * 2
                output.append(new_score)
            elif operations[i] == "C":
                output.pop()
            else:
                output.append(int(operations[i]))
 
        return sum(output)