import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int s = 0;
        for (int i = 0; i < n; i++) {
            int q = Integer.parseInt(br.readLine().replace("6", "9").replace("0", "9"));
            if (q > 100) q = 100;
            s += q;
        }
        bw.write(Math.round((double) s / (double) n) + "");
        bw.flush();
    }
}