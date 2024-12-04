import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        if (n == 0) {
            bw.write("divide by zero");
        } else {
            String[] arr = br.readLine().split(" ");
            bw.write(String.format("%.2f", (double) 1));
        }
        bw.flush();
    }
}