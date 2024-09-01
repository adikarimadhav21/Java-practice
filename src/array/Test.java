package array;

public class Test {

    public static void main(String[] args) {
        String pwrd="796115110113721110141108";
        char a[]=pwrd.toCharArray();
        String res="";

        int i=0;
        for (i=a.length-1;i>0;i=i-2){
            String s= String.valueOf(a[i]+a[i-1]);
            int x= Integer.parseInt(s);
            if (x==32)  res=res+" ";
            else if (x>64 && x<91 || x>89 && x<100){
                res=res+String.valueOf((char)x);
            }
            else {
                 if (i-2<0) break;
                 s+=a[i-2];
                 x=Integer.parseInt(s);
                 res=res+(char)x;
                 i-=1;
            }



        }

        System.out.println(res);
    }
}
