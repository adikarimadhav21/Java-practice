package linkedlist;



public class ReverseList {
    
    public static Node reverse(Node head){
       Node current=head;
       Node prev=null;
       Node next=null;

       while(current!=null){
           next=current.next;
           // font insert
           current.next=prev; // prev bcz reverse pointer not available in sll
           prev=current;
           current=next;
       }

        return prev;
    }

    public static boolean isPalindrome(Node head){
        // 1) store in stack... pop out and compare
        // 2) reverse linklist ... compare each element both list
        // 3) only compare half a) count and second list from middle reverse and compare b) slow >> 1 speed >> fast 2 speed then compare

        Node slow=head;
        Node fast=head;
        while(fast!=null){
            slow=slow.next;
            fast=fast.next.next;
        }

        Node rev_slow=reverse(slow);

        while (rev_slow!=null){

            if(rev_slow.data!= head.data) return  false;
            rev_slow=rev_slow.next;
            head= head.next;
        }

        return  true;
    }

    public static void main(String[] args) {
        SingleLinkedList list1 = new SingleLinkedList();
        list1.insertAtFront(5);
        list1.insertAtFront(4);
        list1.insertAtFront(3);
        list1.insertAtFront(2);
        list1.insertAtFront(1);


        Node b=list1.head;
        while(b!=null){
            System.out.println("b.data = " + b.data);
            b=b.next;

        }

        Node i=reverse(list1.head);
        while(i!=null){
            System.out.println("i.data = " + i.data);
            i=i.next;

        }


        SingleLinkedList list2=new SingleLinkedList();
        list2.insertAtTail(1);
        list2.insertAtTail(2);
        list2.insertAtTail(2);
        list2.insertAtTail(1);
        //list2.printAll();
       Boolean flag= isPalindrome(list2.head);
        System.out.println("flag = " + flag);
    }
}
