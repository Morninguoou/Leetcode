class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        cur = head
        carry = 0
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        while l1 or l2 or carry:
            total = val1 + val2 + carry
            data = total % 10
            carry = total // 10
            cur.next = ListNode(data)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            cur = cur.next
        return head.next