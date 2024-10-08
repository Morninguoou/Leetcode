class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode(0)
        cur = head
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
            elif list1 and not list2:
                cur.next = list1
                list1 = list1.next
            elif list2 and not list1:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        return head.next