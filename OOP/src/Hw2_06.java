import java.util.Scanner;

public class Hw2_06 {

    public static void main(String[] args) {

        System.out.println("1~99 사이의 정수를 입력하시오 >> ");
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = a % 10;
        int c = a % 30;
        if (b == 3 || b == 6 || b == 9){
            System.out.print("박수짝");
            if ((a%3==0) && c != 0)
                System.out.println("짝");
        }
        else
            System.out.println("박수 x");

        sc.close();
    }
}
