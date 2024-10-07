import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        long n, b;
        long[] arr = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();
        n = arr[0];
        b = arr[1];
        long s = 0;
        for (int i = 0; i <= b; i++) {
            s += 1L << i;
        }
        if (n <= s) bw.write("yes");
        else bw.write("no");
        bw.flush();
    }
}