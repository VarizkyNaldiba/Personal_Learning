import java.util.Scanner;

public class Assignment3wri {
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        int midTerm, finlExam, quizSc, assScore;
        double theFinal;
        System.out.println("Mid Test");
        midTerm=input.nextInt();
        System.out.println("Final Exam");
        finlExam=input.nextInt();
        System.out.println("Quiz Score");
        quizSc=input.nextInt();
        System.out.println("Assignment Score");
        assScore=input.nextInt();


        theFinal = (midTerm*0.3) + (finlExam*0.4) + (quizSc*0.1) + (assScore*0.2);
        System.out.println("The Final Score:" + theFinal);
        if (theFinal < 65) {
            System.out.println("The Student Will get remedy:" + theFinal);
        } else {
            System.out.println("The Student Will not get remedy:" + theFinal);
        }





    }
}