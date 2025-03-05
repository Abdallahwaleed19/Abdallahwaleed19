import java.util.Scanner;

public class test13 {
    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner input = new Scanner (System.in);
        int option ;
        int num1 = 100;
        int num2 = 50 ; 
        do
        {
            System.out.println("Choose option from menu : ");
            option = input.nextInt();
            switch(option)  {
                case 1 :
                    System.out.println("The answer of num1+num2 is = "+num1+num2);
                    break;
                case 2 :
                    System.out.println("The answer of num1-num2 is = "+(num1-num2));
                    break;
                case 3 :
                    System.out.println("The answer of num1/num2 is = "+num1/num2);
                    break;
                default :
                    System.out.println("Good Bye");        
            }
            
        }
        while (option!=0);
        
    }
    
}

