import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            long a = Long.parseLong(s[0]);
            long b = Long.parseLong(s[1]);
            StringBuilder ans = new StringBuilder();
            while (a >= b) {
                long mod = a % b;
                a = (a - mod) / b;
                if (mod >= 10) {
                    ans.append((char) (mod - 10 + 'A'));
                } else {
                    ans.append(mod);
                }
            }
            if (a >= 10) {
                ans.append((char) (a - 10 + 'A'));
            } else {
                ans.append(a);
            }
            String res = ans.toString();
            ans.reverse();
            if (res.contentEquals(ans)) {
                bw.write("1\n");
            } else {
                bw.write("0\n");
            }
        }
        bw.flush();
    }
}