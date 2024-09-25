import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0) break;
            int cnt = 0;
            int[] arr = new int[n];
            String[] st = br.readLine().split(",");
            for (String s: st) {
                if (s.contains("-")) {
                    int a = Integer.parseInt(s.split("-")[0]);
                    int b = Integer.parseInt(s.split("-")[1]);
                    if (a > b) continue;
                    for (int i = a; i <= b; i++) {
                        if (i <= n) {
                            arr[i - 1] = 1;
                        }
                    }
                } else {
                    int page = Integer.parseInt(s);
                    if (page <= n) {
                        arr[page - 1] = 1;
                    }
                }
            }
            for (int i: arr) if (i == 1) {
                cnt += 1;
            }
            System.out.println(cnt);
        }
    }
}