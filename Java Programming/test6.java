import java.util.Scanner;

public class test6 {
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("PLease Enter your bais : ");
        double  bais = input.nextDouble();
        System.out.print("PLease Enter your height : ");
        double  Height = input.nextDouble();
        double area = 0.5 * bais * Height ;
        System.out.print("The area is = "+area);


    }
}
