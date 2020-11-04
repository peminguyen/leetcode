# https://leetcode.com/problems/add-two-numbers/submissions/
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        c = 0
        root = None
        node = None
        while l1 or l2:
            res = 0
            if l1:
                res += l1.val
                l1 = l1.next
            if l2:
                res += l2.val
                l2 = l2.next
            res += c
            if res >= 10:
                c = 1
            else:
                c = 0
            res %= 10
            
            if not root:
                root = ListNode(res)
                node = root
            else:
                node.next = ListNode(res)
                node = node.next
        if c:
            node.next = ListNode(c)
        return root