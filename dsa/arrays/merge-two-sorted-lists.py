"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        out = ListNode()
        curr = out
        head1, head2 = list1, list2
        while head1 and head2:
            val_1 = head1.val if head1 else 101
            val_2 = head2.val if head2 else 101
            if val_1 <= val_2:
                curr.next = head1
                if head1:
                    head1 = head1.next
            else:
                curr.next = head2
                if head2:
                    head2 = head2.next
            curr = curr.next
        if head1:
            curr.next = head1
        if head2:
            curr.next = head2
        return out.next


if __name__ == "__main__":
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    # Convert list to linked list
    head1 = ListNode()
    head2 = ListNode()
    curr = head1
    for i in list1:
        curr.next = ListNode(i)
        curr = curr.next

    curr = head2
    for i in list2:
        curr.next = ListNode(i)
        curr = curr.next
    s = Solution()
    print(s.mergeTwoLists(head1.next, head2.next))
