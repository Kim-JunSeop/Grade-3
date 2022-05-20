import java.util.Scanner;
public class Hw3_08 {
    public static void main(String[] args) {
        System.out.print("정수 몇개? >> ");
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int [] arr = new int[num];

        for(int i=0; i<arr.length; i++) {
            int r = (int)(Math.random()*100+1);
            int check = 0;
            for(int j=0; j<arr.length; j++) {
                if(r == arr[j]) {
                    check=1;
                    break;
                }
            }
            if(check == 1) {
                i--;
                continue;
            }
            arr[i] = r;
        }
        for(int i=0; i<arr.length; i++) {
            if(i%10 == 0 && i != 0) System.out.println();
            System.out.print(arr[i] + " ");
        }
        sc.close();
    }
}