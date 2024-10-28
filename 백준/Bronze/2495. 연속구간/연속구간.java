import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int maxcnt, nowcnt = 0;
        for (int i = 0; i < 3; i++) {
            char[] arr = br.readLine().toCharArray();
            nowcnt = maxcnt = 1;
            for (int j = 0; j < 7; j++) {
                if (arr[j] == arr[j + 1]) nowcnt++;
                else {
                    if (maxcnt < nowcnt) {
                        maxcnt = nowcnt;
                    }
                    nowcnt = 1;
                }
            }
            if (maxcnt < nowcnt) {
                maxcnt = nowcnt;
            }
            bw.write(maxcnt + "\n");
        }
        bw.flush();
    }
}