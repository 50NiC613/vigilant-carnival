
class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
class Patrones:
     
     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1
        # actualizando punteros
        while right:
            left = left.next
            right = right.next

        # borrando el nodo
        left.next = left.next.next
        return dummy.next