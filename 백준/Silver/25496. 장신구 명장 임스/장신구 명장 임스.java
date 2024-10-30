import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int p = sc.nextInt(), n = sc.nextInt(), cnt = 0;
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        for(int i: Arrays.stream(a).sorted().toArray()) {
            if (p >= 200) break;
            p += i;
            cnt += 1;
        }
        bw.write(cnt + "");
        bw.flush();

    }
}