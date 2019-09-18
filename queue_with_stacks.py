from collections import deque

class MyQueue():
    oldest_on_top = deque()
    newest_on_top = deque()
    def __init__(self):
       #self.oldest_on_top = deque()
       #self.newest_on_top = deque()
       pass


    def shift_stacks(self):
        if len(self.oldest_on_top)==0 :
            while(len(self.newest_on_top) != 0):
                self.oldest_on_top.append(self.newest_on_top.pop())

    def enqueue(self, value):
        self.newest_on_top.append(value)
        return
    def peek(self):
        self.shift_stacks()
        return self.oldest_on_top[-1]
    def deque(self):
        self.shift_stacks()
        return self.oldest_on_top.pop()


def main():
    mq = MyQueue()
    mq.enqueue(1)
    mq.enqueue(2)
    mq.enqueue(3)
    mq.enqueue(4)

    print(mq.deque())
    print(mq.peek())
if __name__=="__main__":
    main()