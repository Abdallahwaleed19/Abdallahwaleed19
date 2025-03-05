import java.util.Scanner;
public class test8 {
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);
        System.out.print("Enter your number : ");
        int num ;
        num = input.nextInt();
        if (num > 0 ){
            System.out.println("Postive");
              }
        else {
            System.out.println("Negative ");
        }      


    }
    
}
