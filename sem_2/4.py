from LLlist import *


def removeElements(head, data):
    dummy = Node()
    dummy.next = head
    prev = dummy
    cur = head

    while (cur != None):
        if (cur.data == data):
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    return dummy.next
