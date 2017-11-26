class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None  

class LinkedList:
    def __init__(self): 
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        temp=self.head
        if self.head == None :	
            self.head = new_node
        else:
            while(temp.next != None):
                temp=temp.next
            temp.next=new_node
            new_node.next=None
        return self.head
 

    def insertAfter(self, prev_node, new_data):
         if prev_node is None:
            print ("The given previous node must inLinkedList.")
            return
         new_node = Node(new_data)
         new_node.next = prev_node.next
         prev_node.next = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
   
    def InsertNth(self, data, position):
        new=Node(data)
        n=position
        temp=self.head
        if(self.head == None):
            self.head=new
        elif(n==0 and self.head!=None):
            new.next=self.head
            self.head=new
        elif(n==1):
            if(self.head.next==None):
                self.head.next=new
            else:
                new.next=self.head.next
                self.head.next=new
        elif(n==2):
            temp=temp.next
            if(temp.next is None):
                temp.next=new
                new.next=None
            else:
                new.next=temp.next
                temp.next=new
        else:
            c=0
            while(c<=n-2):
                temp=temp.next
                c=c+1
                
            new.next=temp.next
            temp.next=new
            
    def Delete(self, position):
        temp=self.head
        temp2=self.head
        n=position
        c=1
        d=1
        if(n==0):
            self.head=self.head.next
            temp.next=None
            temp2.next=None
        else:
            while(c<=n):
                temp=temp.next
                c=c+1
            while(d<n):
                temp2=temp2.next
                d=d+1
            temp2.next=temp.next
            temp.next=None
     
    def ReversePrint(self):
        temp=self.head
        l1=[]
        if(self.head==None):
            return 
        else:
            while(temp.next != None):
                l1.append(temp.data)
                temp=temp.next
            if(temp.next==None):                                       #Take the last number too
                l1.append(temp.data)
            l2=list(reversed(l1))                                    #Always take the list
            n=len(l2)
            for i in range(n):
                print(l2[i])  
                   
    def Reverse(self):                              #####Method is Important...Remember this
        temp=self.head
        last=None
        while(temp!=None):
            next=temp.next
            temp.next=last
            last=temp
            temp=next
        return last
    
    def CompareLists(self, selfb):
        temp=self.head
        temp2=selfb.head
        c=0
        d=0
        while(temp.next!=None):
            c=c+1
            temp=temp.next
        while(temp2.next!=None):
            d=d+1
            temp2=temp2.next
        if(c!=d):
            return 0
        else:
            temp=self.head
            temp2=selfb.head
            flag=1
            while(temp!=None):
                if(temp.data!=temp2.data):
                    flag=0
                temp=temp.next
                temp2=temp2.next
            if(flag==0):
                print("Not equal")
            else:
                print("Equal")
    
    def RemoveDuplicates(self):
        temp=self.head
        while(temp!=None):
            temp2=temp.next
            while(temp2!=None):
                if(temp.data==temp2.data):
                    temp3=temp
                    while(temp3.next!=temp2):
                        temp3=temp.next
                    temp3.next=temp2.next
                temp2=temp2.next
            temp=temp.next
            
ll = LinkedList()
ll.InsertNth(3,0)
ll.InsertNth(5,1)
ll.InsertNth(7,2)
ll.InsertNth(2,3)
ll.InsertNth(10,1)
ll.InsertNth(5,1)

ll.RemoveDuplicates()
ll.printList()
