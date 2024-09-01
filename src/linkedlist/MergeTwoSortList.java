package linkedlist;

class NodeList {
    int data;
    NodeList next;

    NodeList(int value) {
        this.data = value;
        next = null;
    }
}

public class MergeTwoSortList {
    NodeList head,tail;
    MergeTwoSortList(){
         head=tail=null;
    }



    public NodeList insertSort(int value) {

        NodeList newNode = new NodeList(value);

        if (head == null) {
            head =tail= newNode;
        } else if (head.data > value) {
            newNode.next = head;
            head = newNode;
        }
        else {
            NodeList travel = head;
            while (travel.next != null && travel.next.data < value) {
                travel = travel.next; // previous node
            }

                newNode.next = travel.next;
                travel.next = newNode;



        }
        return  head;


    }

    public NodeList mergeSortedList(NodeList list1 , NodeList list2){
        NodeList head;
        NodeList temp;
        if(list1==null) return list2;
        if(list2==null) return list1;
        if(list1.data<list2.data){
            head= temp= new NodeList(list1.data);
            list1=list1.next;
        }
        else {
            head= temp= new NodeList(list2.data);
            list2=list2.next;
        }
        while (list1.next!=null && list2.next!=null){
            if(list1.data<list2.data){
                temp.next= new NodeList(list1.data);
                list1=list1.next;
            }
            else {
                temp.next= new NodeList(list2.data);
                list2=list2.next;
            }
            temp=temp.next;
        }
        while (list1.next!=null ){
            temp.next= new NodeList(list1.data);
            list1=list1.next;
            temp=temp.next;
        }
        while (list2.next!=null){
            temp.next= new NodeList(list2.data);
            list2=list2.next;
            temp=temp.next;
        }
        return  head;
    }


    public void printList() {
        NodeList transversal = head;
        while (transversal.next != null) {
            System.out.print(transversal.data + " ");
            transversal = transversal.next;
        }
        System.out.println();
    }

    public void printList(NodeList transversal ) {
        while (transversal.next != null) {
            System.out.print(transversal.data + " ");
            transversal = transversal.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        MergeTwoSortList list = new MergeTwoSortList();
        list.insertSort(10);
        list.insertSort(1);
        list.insertSort(6);
        list.insertSort(9);
        NodeList l1=list.insertSort(2);
       // list.insertSort(8);

        MergeTwoSortList list1 = new MergeTwoSortList();
        list1.insertSort(4);
        list1.insertSort(3);
        list1.insertSort(6);
        NodeList l2= list1.insertSort(8);
        // list.insertSort(8);
        list.printList(l1);
        list1.printList(l2);

        MergeTwoSortList merge = new MergeTwoSortList();
        NodeList mergeList=merge.mergeSortedList(l1,l2);
        merge.printList(mergeList);

    }
}
