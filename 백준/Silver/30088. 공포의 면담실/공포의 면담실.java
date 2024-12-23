import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        long ans = 0, sum = 0;
        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            for (int j = 1; j < s.length; j++) {
                arr[i] += Integer.parseInt(s[j]);
            }
        }
        Arrays.sort(arr);
        for (int i = 0; i < n; i++) {
            sum += arr[i];
            ans += sum;
        }
        bw.write(ans + "");
        bw.flush();
    }
}