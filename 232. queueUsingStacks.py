class MyQueue:

    def __init__(self):
        self._a = []
       
        
    def push(self, x: int) -> None:
        temp = []
        for _ in range(len(self._a)):
            temp.append(self._a.pop())
        temp.append(x)
        for i in range(len(temp)):
            self._a.append(temp.pop())
    

    def pop(self) -> int:
        return self._a.pop()
        

    def peek(self) -> int:
        return self._a[-1]
        

    def empty(self) -> bool:
        return self._a == []