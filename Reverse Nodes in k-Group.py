# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.(LeetCode: Hard) (Did additional challenge of doing it in O(1) extra space. It runs in 0 ms which is a bug, so unfortunately do not have time benchmark)
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        check = 0
        second = None
        answer = None
        while True:
            head2 = head
            counter = 0
            check = 0
            while check < k and head2:
                check += 1
                head2= head2.next
            if check < k:
                if second:
                   second.next = head
                break
            first = head
            prev = None
            while counter < k:
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
                counter += 1
            
            if answer == None:
                answer = prev
            if second:
                second.next = prev
            
            second = first
        return answer
