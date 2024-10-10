import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine()), ans = 0;
        while (n != 0) {
            ans += 1;
            if (String.valueOf(ans).contains("666")) n -= 1;
        }
        bw.write(ans + "\n");
        bw.flush();
    }
}