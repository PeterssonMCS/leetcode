# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        k = []
        flag = True
        while(flag):
            if list1 != None :
                try:
                    if list1.val<=list2.val:
                        k.append(list1.val)
                        list1 = list1.next
                except:
                    k.append(list1.val)
                    list1 = list1.next
            if list2 != None :
                try:
                    if list1.val>list2.val:
                        k.append(list2.val)
                        list2 = list2.next
                except:
                    k.append(list2.val)
                    list2 = list2.next
            if list1 == None and list2 == None:
                flag = False
                
        k.reverse()
        list3 = ListNode()
        if k == []:
            return None
        list3.val = k[0]
        for i in k[1:]:
            temp = ListNode()
            temp.val = i
            temp.next = list3
            list3 = temp
        return list3
