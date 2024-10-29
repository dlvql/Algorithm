import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int s = arr[0], e = 0, m = 0;
        for (int i = 1; i < n; i++) {
            e = arr[i - 1];
            if (arr[i - 1] >= arr[i]) {
                if (m < e - s) m = e - s;
                s = arr[i];
                e = arr[i];
            }
        }
        if (arr[n - 1] > arr[n - 2]) e = arr[n - 1];
        if (m < e - s) m = e - s;
        bw.write(m + "");
        bw.flush();

    }
}