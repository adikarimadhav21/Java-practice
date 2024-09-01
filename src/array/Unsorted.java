package array;

public class Unsorted {
    //insert at the end of array
    static  int insertItem(int [] arr,int item,int pos,int cap){
        if (pos>cap){
            System.out.println("Out of range");
            return pos;
        }
        arr[pos]=item;
        return pos+1;
    }

    //2. Insert at any position

    static int insertItem(int []arr, int item, int post){
        for (int i=arr.length-1;i>post;i--){
            arr[i]=arr[i-1];
        }
        arr[post]=item;

        return post+1;

    }

    //search
    static int searchItem(int []arr, int item){
        for (int i=0;i<arr.length;i++){
            if(arr[i]==item)
                return i;
        }

        return item;

    }
    //delete item
    static void deleteItem(int []arr, int pos){

        for (int i=pos;i<arr.length-1;i++){
            arr[i]=arr[i+1];
        }
    }



    public static void main(String[] args) {
        int arr[]=new int[5];
        arr[0]=2;
        arr[1]=3;
        arr[2]=20;
        arr[3]=80;
//        int value=20;
//        int cap=insertItem(arr,value,4,arr.length);
//        for ( int item :arr){
//            System.out.println(item);
//        }
        int pos=1;
        int value=30;
        int cap=insertItem(arr,value,pos);
//        for (int i :arr){
//            System.out.println(i);
//        }

        int index=searchItem(arr,20);
        System.out.println(index);
        deleteItem(arr,index);
        for (int i :arr){
            System.out.println(i);
        }








    }
}


