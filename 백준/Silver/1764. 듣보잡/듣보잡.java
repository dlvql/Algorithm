import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        String[] ans = new String[Math.max(arr[0], arr[1])];
        Set<String> set = new HashSet<>();
        for (int i = 0; i < Math.max(arr[0], arr[1]); i++) ans[i] = "zzzzzzzzzzzzzzzzzzzzzzzz";
        int top = 0, idx = 0;
        for (int i = 0; i < arr[0]; i++) {
            set.add(br.readLine());
            top += 1;
        }
        for (int i = 0; i < arr[1]; i++) {
            String now = br.readLine();
            set.add(now);
            top += 1;
            if (top != set.size()) {
                ans[idx] = now;
                top -= 1;
                idx += 1;
            }
        }
        bw.write(idx + "\n");
        Arrays.sort(ans);
        for (int i = 0; i < idx; i++) {
            bw.write(ans[i] + "\n");
        }
        bw.flush();
    }
}