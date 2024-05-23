from LLlist import *


def hasCycl(head):
    if head is None or head.next is None:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


lol = LinkedList()

cur=lol.head
for i in range (10):
    lol.append_front(i)


lol.print_list()
lok=LinkedList
for i in range (10):
    lok.append_front(i)

print(hasCycl(lol))
print(hasCycl(lok))

