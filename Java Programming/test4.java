
import java.util.Scanner;

public class test4 {
    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner input = new Scanner(System.in);
        int length , width, area ; 
        System.out.println("Please enter length : ");
        length = input.nextInt();
        System.out.println("Please enter width : ");
        width = input.nextInt();
        area = length * width ; 
        System.out.println("The area of rectangle is =  " + area);

        
    }
    
}
