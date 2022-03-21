# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        k = []
        carrier = 0
        while (1):
            s = 0
            if l1 != None:
                s = s + l1.val
                l1 = l1.next
            if l2 != None:
                s = s + l2.val
                l2 = l2.next
            s = s + carrier    
            
            if s >= 10:
                carrier = 1
                s = s - 10
            else:
                carrier = 0
                
            k.append(s)   
            
            if l1 == None and l2 == None:
                if carrier == 1:
                    k.append(carrier)
                break
                
        k.reverse()
        
        l3 = ListNode()
        l3.val = k[0]
        
        for i in range(1,len(k)):
            l_temp = ListNode()
            l_temp.val = k[i]
            l_temp.next = l3
            l3 = l_temp
            
        return l3
