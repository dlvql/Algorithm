import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i = 0; i < 3; i++) {
            int cnt = 0;
            int[] yut = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            for (int n: yut) cnt += n;
            if (cnt == 0) bw.write("D\n");
            else if (cnt == 1) bw.write("C\n");
            else if (cnt == 2) bw.write("B\n");
            else if (cnt == 3) bw.write("A\n");
            else bw.write("E\n");
        }
        bw.flush();
    }
}