class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        o_list = []
        cur = head
        while cur != None:
            o_list.append(cur.val)
            cur = cur.next
        for i in range(len(o_list)):
            if i % 2 != 0:
                temp = o_list[i-1]
                o_list[i-1] = o_list[i]
                o_list[i] = temp
        if len(o_list) == 0:
            return None
        h = ListNode(o_list[0])
        cur = h
        for n in range(1, len(o_list)):
            cur.next = ListNode(o_list[n])
            cur = cur.next
        
        return h