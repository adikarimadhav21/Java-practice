package linkedlist;

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.ListIterator;

public class MergeListCollection {

    public  static void insertSort(LinkedList<Integer> list,int val){

        ListIterator<Integer> iterator= list.listIterator();

        while(iterator.hasNext()){
            if(iterator.next()>val){
                iterator.previous();
                iterator.add(val);
                return;
            }
        }
        iterator.add(val);

    }
    public static void insertSortCol(LinkedList<Integer> list,int val){
        list.add(val);
    }

    public static void mergedList(LinkedList<Integer> merge,LinkedList<Integer> list1,LinkedList<Integer> list2){
        merge.addAll(list1);
        merge.addAll(list2);
    }

    public static void main(String[] args) {
        LinkedList<Integer> list1=new LinkedList<>();
        insertSortCol(list1,10);
        insertSortCol(list1,1);
        insertSortCol(list1,6);
        insertSortCol(list1,9);
        Collections.sort(list1);
        for (int item :list1){
            System.out.print(item+" ");
        }
        System.out.println();

        LinkedList<Integer> list=new LinkedList<>();
        insertSort(list,10);
        insertSort(list,1);
        insertSort(list,6);
        insertSort(list,9);
        for (int item :list){
            System.out.print(item+" ");
        }
        System.out.println();
        LinkedList<Integer> merge=new LinkedList<>();
        mergedList(merge,list,list1);
        Collections.sort(merge);
        for (int item :merge){
            System.out.print(item+" ");
        }
        System.out.println();




    }

}
