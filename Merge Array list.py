class Solution(object):
    def mergeTwoLists(self, list1, list2):
      y=[]
      while list1:
        y.append(list1.val)
        list1=list1.next

      while list2:
        y.append(list2.val)
        list2=list2.next
      y.sort()
      dummy = ListNode(0)
      curr = dummy
      for val in y:
        curr.next = ListNode(val)           
        curr = curr.next
            
      return dummy.next
