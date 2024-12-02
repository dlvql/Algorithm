import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] arr = br.readLine().split(" ");
        int a = Integer.parseInt(arr[0]), b = Integer.parseInt(arr[1]), c = Integer.parseInt(arr[2]);
        bw.write(Math.max(0, Math.max((b - a - 1), (c - b - 1))) + "");
        bw.flush();
    }
}