class MinStack:

    def __init__(self):
        self.min = None
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min == None or val < self.min:
            self.min = val
        

    def pop(self) -> None:
        popped = self.stack.pop()
        if self.stack:
            if popped == self.min:
                self.min = min(self.stack)
        else:
            self.min = None
        return popped
        

    def top(self) -> int:
        if min != None:
            return self.stack[-1]
        else:
            return None
        

    def getMin(self) -> int:
        return self.min
        
