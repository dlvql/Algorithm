import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int cnt = 0;
        for (int i = 1; i <= arr[0]; i++) {
            cnt += 1;
            while (String.valueOf(cnt).contains(String.valueOf(arr[1]))) {
                cnt += 1;
            }
        }
        bw.write(String.valueOf(cnt));
        bw.flush();
    }
}