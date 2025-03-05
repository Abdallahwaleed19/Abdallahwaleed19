import java.util.Scanner;
public class test7 {
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);
        System.out.print("Please Enter x,y,z :");
        double x = input.nextDouble();
        double y = input.nextDouble();
        double z = input.nextDouble();
        double avg = ((x+y+z)/3);
        System.out.println("the average is = "+avg);
        
    }
}
 
