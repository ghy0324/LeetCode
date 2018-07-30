# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        tmp = head
        nodes = []
        for i in range(k):
            if not tmp:
                return head
            nodes.append(tmp)
            tmp = tmp.next
        head.next = self.reverseKGroup(tmp, k)
        for i in range(1, k):
            nodes[i].next = nodes[i - 1]
        head = nodes[k - 1]
        return head