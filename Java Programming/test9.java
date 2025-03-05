
import java.util.Scanner;

public class test9 {
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);
        System.out.print("Enter your grade : ");
        int grade ;
        grade = input.nextInt();
        if (grade >=90){
            System.out.println("A");
        }
        else if (grade >=80){
            System.out.println("B");
        }    
        else if (grade >=70){
            System.out.println("C");
        }
        else if (grade >= 60 ){
            System.out.println("D");
         }
         else{
            System.out.println("You are faild ");
        }    
        
    }
    
}
