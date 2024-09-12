import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[3];
        arr[0] = sc.nextInt();
        arr[1] = sc.nextInt();
        arr[2] = sc.nextInt();
        arr = Arrays.stream(arr).sorted().toArray();
        if (arr[0] + arr[1] <= arr[2]) arr[2] = arr[1] + arr[0] - 1;
        System.out.println(arr[0] + arr[1] + arr[2]);
    }
}