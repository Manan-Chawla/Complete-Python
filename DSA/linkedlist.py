class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None
# creating a node for linked list 
# which contains data and address or link of next node


# creating linekd list
# insert_at_end method will add elememt from last always
# prints works like traverse operation
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert_at_end(self,data):
        new_node=Node(data)
        
        if self.head==None:
            self.head=new_node
            return
        
        current=self.head
        while current.next:
            current=current.next
        
        current.next = new_node    
            
    def prints(self):
        current=self.head
        while current:
            print(current.data,end="--->")
            current=current.next
        print("none")

mylist=LinkedList()
mylist.insert_at_end(10)
mylist.insert_at_end(20)
mylist.insert_at_end(30)
mylist.insert_at_end(40)
mylist.prints()        
        