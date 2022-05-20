import java.util.Scanner;

public class Hw2_02 {

    public static void main(String[] args) {

        System.out.println("2자리 정수를 입력(10~99)>>");
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int a = num/10;
        int b = num%10;
        if (a == b)
            System.out.println("Yes! 10의 자리와 1의 자리가 같습니다.");
        else if(a != b)
            System.out.println("No! 10의 자리와 1의 자리가 다릅니다.");
        else
            System.out.println("숫자를 입력하시오");


        sc.close();

    }
}
