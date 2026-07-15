class FreqStack:

    def __init__(self):
        # value -> frequency
        self.counts = {}

        # frequency -> stack of values
        self.groups = {}

        # current maximum frequency
        self.maxFreq = 0

    def push(self, val: int) -> None:
        # Increase this value's frequency
        freq = self.counts.get(val, 0) + 1
        self.counts[val] = freq

        # Create a stack for this frequency if needed
        if freq not in self.groups:
            self.groups[freq] = []

        # Add this value to its frequency stack
        self.groups[freq].append(val)

        # Update the maximum frequency
        self.maxFreq = max(self.maxFreq, freq)

    def pop(self) -> int:
        # Pop the most recently inserted value
        # from the highest frequency stack
        val = self.groups[self.maxFreq].pop()

        # Decrease its frequency
        self.counts[val] -= 1

        # If that frequency stack is empty,
        # we've lost the maximum frequency
        if not self.groups[self.maxFreq]:
            self.maxFreq -= 1

        return val