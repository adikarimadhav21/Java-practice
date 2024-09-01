package linkedlist;

public class AddTwo {

    /***
     * Example:
     * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
     *
     * Output: 7 -> 0 -> 8
     *
     * Explanation: 342 + 465 = 807.
     */

    public static Node addNumber(Node l1, Node l2) {
        Node head = null;
        Node temp = head;
        int carry = 0;
        while (l1 != null || l2 != null) {
            int sum = carry;
            if (l1 != null) {
                sum += l1.data;
                l1 = l1.next;
            }
            if (l2 != null) {
                sum += l2.data;
                l2 = l2.next;
            }
            Node new_node = new Node(sum % 10);
            carry = sum / 10;
            if (temp == null) head = temp = new_node;
            else {
                temp.next = new_node;
                temp = temp.next;
            }
        }
        if (carry > 0) temp.next = new Node(carry);

        return head;
    }

    public static void main(String[] args) {
        SingleLinkedList list1=new SingleLinkedList();
        list1.insertAtTail(2);
        list1.insertAtTail(4);
        list1.insertAtTail(3);
        list1.printAll();
        SingleLinkedList list2=new SingleLinkedList();
        list2.insertAtTail(5);
        list2.insertAtTail(6);
        list2.insertAtTail(4);
        list2.printAll();
        Node result=addNumber(list1.head,list2.head);
        while(result!=null){
            System.out.println("result.data = " + result.data);
            result=result.next;
        }
    }

}
