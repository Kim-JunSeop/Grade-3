import java.util.Scanner;

public class practice {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char grade;

        System.out.println("성적입력");
        int score = sc.nextInt();

        switch (score/10){
            case 10:
            case 9:
                System.out.println("학점은 A 입니다"  );
        }
    }

}

