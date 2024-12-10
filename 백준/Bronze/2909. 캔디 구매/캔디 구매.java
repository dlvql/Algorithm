import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] arr = br.readLine().split(" ");
        int k = Integer.parseInt(arr[1]);
        int c = Integer.parseInt(arr[0]);
        bw.write((int) (Math.round(c / Math.pow(10, k)) * Math.pow(10, k)) + "");
        bw.flush();
    }
}