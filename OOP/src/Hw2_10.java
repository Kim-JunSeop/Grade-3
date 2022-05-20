import java.util.Scanner;

public class Hw2_10 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("첫번째 원의 중심과 반지름 입력 >> ");
        int x1 = sc.nextInt();
        int y1 = sc.nextInt();
        double r1 = sc.nextInt();
        System.out.print("두번째 원의 중심과 반지름 입력 >>  ");
        int x2 = sc.nextInt();
        int y2 = sc.nextInt();
        double r2 = sc.nextInt();

        double distance = Math.sqrt(Math.pow((x2-x1),2)+Math.pow((y2-y1), 2));

        if(r1+r2>=distance)
            System.out.println("두 원은 서로 겹친다.");
        else
            System.out.println("두 원은 서로 겹치지 않는다.");

        sc.close();
    }

}
