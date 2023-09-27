import java.util.Scanner;

public class Selection4 {
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        double number1, number2, result;
        char operator;
        System.out.println("Enter the first number: ");
        number1=input.nextDouble();
        System.out.println("Enter the second number: ");
        number2=input.nextDouble();
        System.out.println("Enter an Operator (+ - * /): ");
        operator=input.next().charAt(0);
        switch (operator) {
            case '+':
                result=number1 + number2; 
                System.out.println(number1 + "+" + number2 + "=" + result);
                break;
            case '-':
                result=number1 - number2;
                System.out.println(number1 + "-" + number2 + "=" + result);
                break;
            case '*':
                result=number1 * number2;
                System.out.println(number1 + "*" + number2 + "=" + result);
                break;
            case '/':
                result=number1 / number2;
                System.out.println(number1 + "/" + number2 + "=" + result);
                break;
            default:
                System.out.println("The Operator you entered is wrong");
        }
    }
}