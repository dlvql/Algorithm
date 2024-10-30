import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] arr = {3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1};
        char[] j = br.readLine().toCharArray(), s = br.readLine().toCharArray();
        int[] g = new int[j.length * 2];
        for (int i = 0; i < j.length; i++) {
            g[i * 2] = arr[j[i] - 'A'];
            g[i * 2 + 1] = arr[s[i] - 'A'];
        }
        for (int i = g.length - 1; i > 1; i--) {
            int[] g1 = g.clone();
            for (int k = 0; k < i; k++) {
                g[k] = (g1[k] + g1[k + 1]) % 10;
            }
        }
        bw.write(g[0] + "" + g[1]);
        bw.flush();

    }
}