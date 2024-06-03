class MyQueue:

    def __init__(self):
        self.a = []

    def push(self, x: int) -> None:
        self.a.append(x)
    def pop(self) -> int:
       return self.a.pop(0)

    def peek(self) -> int:
        if len(self.a):
            return self.a[0]

    def empty(self) -> bool:
        if len(self.a)==0:
            return True
        else : return False

        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(4)
# obj.push(4)

param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

print(param_2,param_3,param_4)

print([1,2]+[3,4])