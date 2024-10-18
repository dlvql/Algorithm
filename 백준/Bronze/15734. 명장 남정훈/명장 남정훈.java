import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int ans = 0;
        if (arr[0] > arr[1]) {
            while (arr[0] > arr[1] && arr[2] > 0) {
                arr[2] -= 1;
                arr[1] += 1;
            }
            arr[0] = arr[1];
        } else if (arr[0] < arr[1]) {
            while (arr[1] > arr[0] && arr[2] > 0) {
                arr[2] -= 1;
                arr[0] += 1;
            }
            arr[1] = arr[0];
        }
        ans += arr[0] + arr[1] + arr[2];
        if (arr[2] % 2 == 1) ans -= 1;
        bw.write(ans + "");
        bw.flush();
    }
}