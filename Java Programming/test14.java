import java.util.Scanner;

public class test14 {
    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);
        int size;
        int sum=0;
        int avg = 0;
        int count = 0;
        System.out.print("Enter size : ");
        size=input.nextInt();
        int[]list_size=new int[size];
        for (int i =0 ; i<list_size.length;i++){
            System.out.print("Enter your numbers : ");
            list_size[i]=input.nextInt();
            if (list_size[i]>0){
                sum +=list_size[i];
            count++;
            }
        }

    System.out.println("The sum is = " + sum);
    System.out.println("The average is = "+ (sum/count));    
    }


}
