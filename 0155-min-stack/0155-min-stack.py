class MinStack:

    def __init__(self):
        self.stack=[]             #all value wala stack
        self.minstack=[]   #Min value wala stack

    def push(self, val: int) -> None:
        self.stack.append(val)   #add value

        if not self.minstack:
            self.minstack.append(val)      #first element
        else:
            current_min=self.minstack[-1]
            self.minstack.append(min(val,current_min))
        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()