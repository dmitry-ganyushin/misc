class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow = head
    fast = head.next
    while (fast is not None and fast.next is not None):
        if fast == slow:
            return True
        fast = fast.next.next
        slow = slow.next
    return False

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("has cycle: " + str(has_cycle(head)))



if __name__=="__main__":
    main()