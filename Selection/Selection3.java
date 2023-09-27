import java.util.Scanner;

public class Selection3 {
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        int age;
        System.out.println("Enter your Age");
        age=input.nextInt();
        if (age > 65) {
            System.out.println("Elderly");
        } else if (age > 18) {
            System.out.println("Adults");
        } else if (age > 12) {
            System.out.println("Teens");
        } else if (age > 5) {
            System.out.println("Children");
        } else {
            System.out.println("Toddler");
        }
    }
}