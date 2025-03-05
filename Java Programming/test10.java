import java.util.Scanner;
public class test10 {
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);
        System.out.print("Enter your choise : ");
        int choise ;
        choise = input.nextInt();
        switch (choise)
        {
            case 1 :
                System.out.print("Enter your numbers : ");
                int num1 = input.nextInt();
                int num2 = input.nextInt();
                System.out.println(num1+num2);
                break;
            
            case 2 :
                System.out.print("Enter your numbers : ");
                int num3 = input.nextInt();
                int num4 = input.nextInt();
                System.out.println(num3*num3);
                System.out.println(num4*num4);
                break;
            
            case 3 :
                System.out.print("Enter your numbers : ");
                int num5 = input.nextInt();
                int num6 = input.nextInt();
                System.out.println(num5-num6);
                break;
            
                   
            default :
                System.out.println("Error input ");

        }
        


    }
    
}
