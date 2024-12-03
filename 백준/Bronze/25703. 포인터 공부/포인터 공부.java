import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        bw.write("int a;\nint *ptr = &a;");
        for (int i = 1; i < n; i++) {
            bw.write("\nint ");
            for (int j = 0; j < i + 1; j++) {
                bw.write("*");
            }
            bw.write("ptr" + (i + 1) + " = &ptr" + (i == 1 ? "" : i) + ";");
        }
        bw.flush();
    }
}