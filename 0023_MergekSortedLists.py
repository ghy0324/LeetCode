# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        numbers = []
        for i in lists:
            while i:
                numbers.append(i.val)
                i = i.next
        numbers.sort()
        if not numbers:
            return None
        ans = ListNode(numbers.pop(0))
        tmp = ans
        while numbers:
            new = ListNode(numbers.pop(0))
            tmp.next = new
            tmp = tmp.next
        return ans