import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int cnt = 0;
        for (int a = 1; a <= n; a++) {
            int[] arr = Arrays.stream(String.valueOf(a).split("")).mapToInt(Integer::parseInt).toArray();
            int s = 0;
            for(int i: arr) {
                s += i;
            }
            if (a % s == 0) cnt += 1;
        }
        bw.write(cnt + "");
        bw.flush();
    }
}