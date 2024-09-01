package array;

public class Sorted {
    // binary search
    static int findElement(int []arr,int item,int low,int high){

        int mid=(low+high)/2;
        if (arr[mid]==item)
            return mid;
        if (item>arr[mid])
            return findElement(arr,item,mid+1,high);
        else
            return findElement(arr,item,low,mid-1);

    }
    //delete item
    static  void deleteItem(int [] arr, int pos){
        for (int i=pos;i<arr.length-1;i++){
            arr[i]=arr[i+1];
        }
    }
    //insert
    static  int insertItem(int[] arr,int val){
        int index = 0;
        for ( int i=0;i<arr.length-1;i++){
            if(arr[i]>=val)
                break;
            index=i;

        }
        for ( int i=index+1;i<arr.length-1;i++){
            arr[i+1]=arr[i];

        }
        arr[index+1]=val;



        return index;

    }


    public static void main(String[] args) {

        int a[]=new int[5];
        a[0]=6;
        a[1]=7;
        a[2]=7;
        a[3]=8;
        a[4]=9;

        int index=findElement(a,8,0,4);
        System.out.println(index);
        deleteItem(a,index);
        for(int item :a){
            System.out.print(" "+item);
        }
        System.out.println();
        int indx=insertItem(a,8);
        for(int item :a){
            System.out.print(" "+item);
        }


    }
}
