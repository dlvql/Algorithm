import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            int m = 1;
            while (n != 1) {
                if (n > m) m = n;
                if (n % 2 == 0) n /= 2;
                else n = n * 3 + 1;
            }
            bw.write(m + "\n");
        }
        bw.flush();
    }
}