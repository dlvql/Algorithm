import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int cnt = 0;
        for (int a = 1; a <= n; a++) {
            int k = a, s = 0;
            while (k > 0) {
                int i = k % 10;
                s += i;
                k = (k - i) / 10;
            }
            if (a % s == 0L) cnt += 1;
        }
        bw.write(cnt + "");
        bw.flush();
    }
}