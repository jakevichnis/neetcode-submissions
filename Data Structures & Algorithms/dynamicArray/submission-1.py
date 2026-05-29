class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.Dynamo = [0] * self.capacity

        # had to create this bit
        self.length = 0
        
        if not capacity:
            print("Array must be greater than 0")
            

    def get(self, i: int) -> int:
        return self.Dynamo[i]

    def set(self, i: int, n: int) -> None:
        self.Dynamo[i] = n



    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        # insert at next empty position
        self.Dynamo[self.length] = n
        self.length += 1    
        


    def popback(self) -> int:    
        if self.length == 0:
            return None    
        self.length -= 1
        return self.Dynamo[self.length] 




    def resize(self) -> None:
        
        self.capacity = self.capacity * 2
        # Create a new array of double capacity
        new_arr = [0] * (self.capacity)

        # copy elements to new array
        for i in range(self.length):
            new_arr[i] = self.Dynamo[i]
        self.Dynamo = new_arr    

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity