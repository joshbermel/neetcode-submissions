# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # need to count total number of nodes on first pass
        # then calculate the node number to be removed (lenght - n)
        # then at that node, store its next temporarily and remove 

        if head == None:
            return None

        node = head
        i = 1
        while node.next != None:
            node = node.next
            i += 1
        
        if i == 1:
            return None

        if n == i:
            node = head
            new_head = node.next
            node.next = None
            return new_head

        remove = i - n + 1

        node = head
        while remove - 2 > 0:
            node = node.next
            remove -= 1

        # the next node is the one being removed
        to_remove = node.next

        # if we are at end of list
        if to_remove.next == None:
            node.next = None
            return head
        
        else:
            node.next = to_remove.next
            to_remove.next = None  

        return head
        


