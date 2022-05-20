public class Hw3_02 {
    public static void main(String[] args) {

        int n[][] = {{1}, {1, 2, 3}, {1, 2, 3, 4}, {1, 2}};

        for (int i = 0; n.length > i; i++) {

            for (int j = 0; n[i].length > j; j++) {

                System.out.print(n[i][j] + " ");
            }
            System.out.println();
        }

    }

}

