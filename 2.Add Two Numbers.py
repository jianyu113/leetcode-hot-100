# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur1 = l1
        cur2 = l2
        carry = 0
        i=0
        dummy = ListNode(0)
        sum_node = dummy
        while (cur1 or cur2 or carry):
            num1 = cur1.val if cur1 else 0
            num2 = cur2.val if cur2 else 0

            sum_of_digits = (num1 + num2 + carry) % 10
            carry = (num1 + num2 + carry) // 10

            sum_node.next = ListNode(sum_of_digits)
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
            sum_node = sum_node.next
        return dummy.next