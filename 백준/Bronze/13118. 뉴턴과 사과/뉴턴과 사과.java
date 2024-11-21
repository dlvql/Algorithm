import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] arr = br.readLine().split(" ");
        String x = br.readLine().split(" ")[0];
        int ans = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].equals(x)) {
                ans = i + 1;
            }
        }
        bw.write(ans +"");
        bw.flush();
    }
}