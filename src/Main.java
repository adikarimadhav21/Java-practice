import java.util.Scanner;

class Solution {

    public int removeDuplicate(int [] nums){
        int count=1;
        int j=0;
        for (int i=j+1;i<nums.length;i++){
            if (nums[j]==nums[i] && count<2){
                count++;
                j++;
                nums[j]=nums[i];


            }
            else if (nums[j]!=nums[i]){
                count=1;
                j++;
                nums[j]=nums[i];
            }


        }
        for (int e :nums){
            System.out.println(e);
        }
        return j+1;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution =new Solution();
        int a []={1,1,1,2,2,3};
        int i=solution.removeDuplicate(a);
        System.out.println(i);


    }
}