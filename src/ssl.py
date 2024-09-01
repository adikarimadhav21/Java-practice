class Node:
    
    def __init__(self,value) -> None:
        self.data=value
        self.next=None
        

class ssl:
    def __init__(self) -> None:
        self.head=None
    def insert_front(self,value):
        new_node=Node(value) 
        new_node.next=self.head
        self.head=new_node

    def tail_insert(self,value):
        new_node=Node(value)
        if(self.head==None):
           self.head=new_node
        else:
            temp=self.head  
            while temp.next!=None:
                temp=temp.next
            temp.next=new_node    

    def delete_sl(self,target):

        if self.head.data==target:
            self.head=self.head.next
        else:
            temp=self.head
            
            while temp.next!=None and temp.data!=target:
                prev=temp
                temp=temp.next
            prev.next=temp.next 
           
    def insert_sort(self,value):
        new_node=Node(value)
        if self.head ==None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next!=None and temp.data<value:  
                prev=temp
                temp=temp.next
            if temp.next==None:
                temp.next=new_node
            else:
                new_node.next=temp
                prev.next=new_node      




    def print_sl(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next    






def main():
   sl=ssl()
   sl.insert_front(2)
   sl.insert_front(5)

   sl.print_sl()
   print("*"*20)
   sl1=ssl()
   sl1.tail_insert(2)
   sl1.tail_insert(5)
   sl1.tail_insert(9)
   sl1.tail_insert(20)

   sl1.print_sl()
   print("*"*20)
   sl1.delete_sl(5)
   sl1.print_sl()
   print("*"*20)

   sl2=ssl()
   sl2.insert_sort(2)
   sl2.insert_sort(5)
   sl2.insert_sort(9)
   sl2.insert_sort(20)

   sl2.print_sl()

if __name__=="__main__":
    main()
