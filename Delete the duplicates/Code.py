class Solution(object):
  def deleteDup(self,head):
    curr=head
    while curr.next!=None:
      if curr.val== curr.next.val:
        tmp= curr.next
        curr.next=curr.next.next
        delete tmp
      else:
        curr=curr.next
      return head 
      
