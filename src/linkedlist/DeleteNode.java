package linkedlist;

public class DeleteNode {

    public static Node deleteNode(Node head,int value){

        Node temp=head;
        Node prev=null;
        if (temp.data==value){
            head=temp.next;
            return head;

        }else {

            while(temp!=null && temp.data!=value){
                prev=temp;
                temp=temp.next;
            }

            if (temp==null) return head;

            prev.next=temp.next;
            return head;

        }
    }

    public static void main(String[] args) {
        SingleLinkedList list=new SingleLinkedList();
        list.insertAtTail(5);
        list.insertAtTail(10);
        list.insertAtTail(30);
        list.insertAtTail(8);
        list.printAll();

        Node head=deleteNode(list.head,30);
        while(head!=null){
            System.out.println("head = " + head.data);
            head=head.next;
        }
    }
}
