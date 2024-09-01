package linkedlist;

import java.util.LinkedList;

class Node {
    int data;
    Node next;

    Node(int value) {
        this.data = value;
        this.next = null;
    }

}

public class SingleLinkedList {

    Node head, tail;

    SingleLinkedList() {
        head = tail = null;
    }

    void insertAtFront(int value) {
        Node new_node = new Node(value);
        new_node.next = head;
        head = new_node;
    }

    void insertAtTail(int value) {

        Node new_node = new Node(value);
        tail= head;
        if (tail == null) {
            head = tail = new_node;
        } else {
            while(tail.next!=null){
                tail=tail.next;
            }
            tail.next = new_node;
        }


    }


    void insertAtBetween(int value, Node previous){
        if(previous==null)
        {
            System.out.println("Invalid");
            return;
        }
        Node new_node=new Node(value);
        new_node.next=previous.next;
        previous.next=new_node;


    }

    void printAll() {
        Node tr=head;

        while (tr != null) {

            System.out.println(tr.data);
            tr = tr.next;
        }
    }


    public static void main(String[] args) {

        SingleLinkedList list = new SingleLinkedList();
        list.insertAtFront(5);
        list.insertAtFront(2);
        list.insertAtFront(10);
        list.insertAtTail(20);
        list.insertAtTail(50);
        list.insertAtBetween(6,list.head);
        list.printAll();

    }
}
