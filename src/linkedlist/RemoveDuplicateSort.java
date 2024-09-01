package linkedlist;

public class RemoveDuplicateSort {

    public static Node remove_dup(Node head){
        Node current=head;
        if (current==null) return head;
        while(current!=null && current.next!=null){
            if(current.data==current.next.data){
                current.next=current.next.next;
            }
            else {
                current=current.next;
            }
        }
        return head;

    }
    public static void main(String[] args) {

        SingleLinkedList l =new SingleLinkedList();
        l.insertAtTail(1);
        l.insertAtTail(1);
        l.insertAtTail(2);
        l.insertAtTail(3);
        l.insertAtTail(3);
        l.printAll();
        Node r=remove_dup(l.head);
        while(r!=null){
            System.out.println("r.data = " + r.data);
            r=r.next;
        }

    }
}
