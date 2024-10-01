import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int[] dots = new int[5];
        for (int i = 0 ; i < n; i++) {
            String[] s = br.readLine().split(" ");
            int x = Integer.parseInt(s[0]), y = Integer.parseInt(s[1]);
            if (x == 0 || y == 0) dots[0] += 1;
            else {
                if (x > 0) {
                    if (y > 0) dots[1] += 1;
                    else dots[4] += 1;
                } else {
                    if (y > 0) dots[2] += 1;
                    else dots[3] += 1;
                }
            }
        }
        for (int i = 1; i <= 4; i++) {
            bw.write("Q" + i + ": " + dots[i] + "\n");
        }
        bw.write("AXIS: " + dots[0]);
        bw.flush();
    }
}