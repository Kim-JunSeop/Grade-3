import java.util.Scanner;

public class Hw2_12_1 {

    public static void main(String[] args) {

        System.out.println("연산>> ");
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        String s = sc.next();
        int b = sc.nextInt();


        if (s.equals("+"))
            System.out.println(a+s+b + "의 계산결과는" + (a+b));
        else if (s.equals("="))
            System.out.println(a + s +  b + "의 계산결과는" + (a==b));
        else if (s.equals("*"))
            System.out.println(a + s +  b + "의 계산결과는" + (a*b));
        else if (s.equals("/")) {
            if (b == 0)
                System.out.println("0으로 나눌 수 없습니다.");
            else
                System.out.println(a + s + b + "의 계산결과는" + (a / b));
        }
        else
            System.out.println("오류입니다");

        sc.close();
    }
}
