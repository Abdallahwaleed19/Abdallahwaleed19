import java.util.Scanner;

public class test11 {
    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);
        int counter = 1;
        int grade = 0 ;
        int sum = 0;
        
        while (counter <=6 ){
            System.out.print("Enter your grade : ");
            grade = input . nextInt();
            sum += grade ;
            counter++ ; 

        }
        System . out . println("The counter = " + counter );
        System . out . println("The sum is = " + sum );
        System . out . println("The average is = " + sum/counter);    
    }
    
}
