def SortedInsert(head, data):
    temp=head
    new=Node(data)
    if(head==None):
        head=new
        return head
    elif(head.data>=new.data):
        new.next=head
        head.prev=new
        head=new
    else:
        while(temp.data<=new.data and temp.next!=None):
            temp=temp.next
        if(temp.data<new.data):
            temp.next=new
            new.prev=temp
            new.next=None
        else:
            temp2=temp.prev
            new.next=temp
            new.prev=temp2
            temp2.next=new
            temp.prev=new
    return head
