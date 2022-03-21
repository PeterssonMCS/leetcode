# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a = []
        v = []
        j = 1
        while(head != None):
            a.append(head.val)
            if j % k == 0:
                a.reverse()
                for m in a:
                    v.append(m)
                a = []
            j = j+1 
            if head != None:
                head = head.next
        for m in a:
            v.append(m)
         
        v.reverse()
        list3 = ListNode()
        list3.val = v[0]
            
        for m in v[1:]:
            temp = ListNode()
            temp.val = m
            temp.next = list3
            list3 = temp
            
        return list3 
