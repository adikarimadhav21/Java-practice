package linkedlist;



public class Intersection {
    // A+ B= B+A
    public static Node intersection(Node l, Node l2){
        Node list1=l,list2=l2;
        if(list1==null || list2==null) return  null;
        while(list1!=list2){
            list1=list1==null?l2:list1.next;
            list2=list2==null?l:list2.next;
        }
        return list1;
    }

    public static void main(String[] args) {
        /**
        Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
        Output: Intersected at '8'
        **/
        SingleLinkedList list1 = new SingleLinkedList();
        list1.insertAtFront(5);
        list1.insertAtFront(4);
        list1.insertAtFront(8);
        list1.insertAtFront(1);
        list1.insertAtFront(4);
        SingleLinkedList list2 = new SingleLinkedList();
        list2.insertAtFront(5);
        list2.insertAtFront(4);
        list2.insertAtFront(8);
        list2.insertAtFront(1);
        list2.insertAtFront(6);
        list2.insertAtFront(5);
        
        Node i=intersection(list1.head,list2.head);
        if (i != null) {
            System.out.println("Intersection found at '" + i.data + "'");
        } else {
            System.out.println("No intersection found");
        }
    }
}
