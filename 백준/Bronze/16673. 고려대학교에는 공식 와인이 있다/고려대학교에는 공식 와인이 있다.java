import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] arr = br.readLine().split(" "); // c, k, p
        int wine = 0;
        int k = Integer.parseInt(arr[1]), p = Integer.parseInt(arr[2]);
        for (int i = 1; i <= Integer.parseInt(arr[0]); i++) {
            wine += (k * i) + (p * i * i);
        }
        bw.write(wine + "");
        bw.flush();
    }
}