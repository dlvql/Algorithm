import java.util.*;

public class Main {
    public void printArray(int[] arr) {
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[5];

        for (int i = 0; i < 5; i++) arr[i] = sc.nextInt();
        int tmp = 0;
        while (arr[0] != 1 || arr[1] != 2 || arr[2] != 3 || arr[3] != 4 || arr[4] != 5) {
            if (arr[0] > arr[1]) {
                tmp = arr[1];
                arr[1] = arr[0];
                arr[0] = tmp;
                for (int i: arr) {
                    System.out.print(i + " ");
                }
                System.out.println();
            } if (arr[1] > arr[2]) {
                tmp = arr[2];
                arr[2] = arr[1];
                arr[1] = tmp;
                for (int i: arr) {
                    System.out.print(i + " ");
                }
                System.out.println();
            } if (arr[2] > arr[3]) {
                tmp = arr[3];
                arr[3] = arr[2];
                arr[2] = tmp;
                for (int i: arr) {
                    System.out.print(i + " ");
                }
                System.out.println();
            } if (arr[3] > arr[4]) {
                tmp = arr[4];
                arr[4] = arr[3];
                arr[3] = tmp;
                for (int i: arr) {
                    System.out.print(i + " ");
                }
                System.out.println();
            }
        }
    }
}