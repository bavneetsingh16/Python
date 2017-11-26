def Reverse(head):
    temp=None
    current=head
    if(head==None):
        return head
    else:
        while(current!=None):
            temp=current.prev
            current.prev=current.next
            current.next=temp
            temp2=current
            current=current.prev
    return temp2