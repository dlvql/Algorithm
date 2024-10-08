import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] n = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int max = -1;
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n[1]; i++) {
            int k = Integer.parseInt(sb.append(n[0] * i).reverse().toString());
            if (k > max) max = k;
            sb.delete(0, sb.length());
        }
        bw.write(max + "\n");
        bw.flush();
    }
}
