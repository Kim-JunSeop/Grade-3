import java.util.Scanner;

public class Hw2_08 {

    public static boolean inRect(int x, int y) {
        if((x >= 100 && x <= 200) && (y >= 100 && y <= 200))
            return true;
        else
            return false;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean result1, result2;

        System.out.println("두 점 ((x1,y1) , (x2,y2))을 입력하시오");
        int x1 = sc.nextInt(); int y1 = sc.nextInt();
        int x2 = sc.nextInt(); int y2 = sc.nextInt();
        result1 = inRect(x1,y1);
        result2 = inRect(x2,y2);

        if(result1 == true || result2 == true)
            System.out.println("(100,100) , (200,200)과 충돌합니다");
        else {
            System.out.println("(100,100) , (200,200)과 충돌하지 않습니다");
        }
        sc.close();
    }
}
