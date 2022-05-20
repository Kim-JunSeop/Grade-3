public class Hw3_10 {

    public static void main(String[] args) {
        int arr[][] = new int[4][4];
        int result = 0;
        while (result < 10) {
            int x = (int) (Math.random() * 4);
            int y = (int) (Math.random() * 4);
            if (arr[y][x] == 0) {
                arr[y][x] = (int) (Math.random() * 10 + 1);
                result++;
            }
        }
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}
