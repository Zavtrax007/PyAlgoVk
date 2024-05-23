from LLlist import *


def mergeSortedLists(head1, head2):
    dummy = Node()
    dummy.next = head1
    p1 = head1
    p2 = head2
    while p1 is not None and p2 is not None:
        if p1.data >= p2.data:
            p2, p2.next = p2.next, p1
        else:
            p1.next, p2 = p2, p2.next
    return head1
