import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int cnt = 0;
        for (int i = 1; i <= n; i++) {
            if (i < 100) cnt++;
            else {
                int a = Integer.parseInt(String.valueOf(String.valueOf(i).charAt(0)));
                int b = Integer.parseInt(String.valueOf(String.valueOf(i).charAt(1)));
                int c = Integer.parseInt(String.valueOf(String.valueOf(i).charAt(2)));
                if (a - b == b - c) cnt++;
            }
        }
        bw.write(cnt + "");
        bw.flush();
    }
}