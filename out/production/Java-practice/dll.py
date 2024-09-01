class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        self.prev=None
class Double_Linked_List:
    def __init__(self):
        self.head=None        
    def insert_front(self,value):
        new_node= Node(value)
        if self.head is None:
            new_node.next=self.head
            self.head=new_node
           # self.head.prev=None
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node    


    def display(self):
         if self.head is None:
             print("No record found")
         else:
             temp=self.head
             while temp is not None:
                 print(temp.data)
                 temp=temp.next    


def main():
   dll= Double_Linked_List()
   dll.insert_front(2)
   dll.insert_front(4)
   dll.insert_front(1)
   dll.insert_front(5)

   dll.display()
if __name__=="__main__":
    main()        