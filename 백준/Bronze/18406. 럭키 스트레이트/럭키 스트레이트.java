import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        char[] arr = br.readLine().toCharArray();
        int l = arr.length / 2;
        int a = 0, b = 0;
        for (int i = 0; i < l; i++) {
            a += Integer.parseInt(String.valueOf(arr[i]));
            b += Integer.parseInt(String.valueOf(arr[i + l]));
        }
        bw.write(a == b ? "LUCKY" : "READY");
        bw.flush();
    }
}