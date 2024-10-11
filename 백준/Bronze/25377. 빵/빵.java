import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int[][] m = new int [n][2];
        int min = 1001;
        for (int i = 0; i < n; i++) {
            m[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            if (m[i][0] <= m[i][1] && min > m[i][1]) {
                min = m[i][1];
            }
        }
        if (min == 1001) min = -1;
        bw.write( min + "\n");
        bw.flush();
    }
}