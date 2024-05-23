from LLlist import *


def centerList(head):
    slow = fast = head
    while fast is not None or fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
