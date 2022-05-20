import java.util.Scanner;

public class Hw2_04 {

    public static void main(String[] args) {

        System.out.println("정수를 3개입력 >> ");
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        if ((a>b && a<c) || (a<b && a>c))
            System.out.println("중간 값은 "+a);
        else if((b>a && b<c) || (b<a && b>c))
            System.out.println("중간 값은 "+b);
        else
            System.out.println("중간 값은 " +c);

        sc.close();
    }
}
