import java.util.Scanner;

public class Selection2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int score;
        System.out.println("Enter a score: ");
        score = input.nextInt();
        if (score >= 100) {
            score += 10;
        } else {
            score -= 10;
        }   
        System.out.println("The Final Score is " + score);
    }
}