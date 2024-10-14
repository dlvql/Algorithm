import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String[] s = br.readLine().split(" ");
        for (String c: s) {
            int l = c.length() - 1;
            if (c.length() % 2 == 1) {
                l -= 1;
            }
            for (int i = 0; i < l; i += 2) {
                int k = (c.charAt(i) - 'a' + c.charAt(i + 1) - 'a') - n;
                if (k < 0) k += 26;
                bw.write((char) (k % 26 + 97));
            }
            bw.write(" ");
        }
        bw.flush();
    }
}