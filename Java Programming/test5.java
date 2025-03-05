import java.util.Scanner ;
public class test5 {
    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner input = new Scanner (System.in);
        System.out.println("Please Enter your Radius : ");
        double r = input.nextDouble();
        double area =  Math.PI * r * r ;
        System.out.println("The area of circle is = " + area );


    }
    
}





