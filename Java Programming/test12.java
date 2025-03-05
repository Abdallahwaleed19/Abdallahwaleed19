import java.util.Scanner;

public class test12 {
    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner input =  new Scanner (System.in);
        int grade = 0;
        int sum = 0;
        int counter = 1 ;
        do
        {
            System.out.print("Enter your grade : ");
            grade = input.nextInt();
            sum += grade ; 
            counter ++ ;
            

        }
        while (counter <=6);
        System.out.println("The average is = "+ sum/counter );
        
        
    }
    
}
