import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int l = Integer.parseInt(br.readLine());
        int a = Integer.parseInt(br.readLine()), b = Integer.parseInt(br.readLine());
        int c = Integer.parseInt(br.readLine()), d = Integer.parseInt(br.readLine());
        int r = Math.max((int) Math.ceil((double) a / c), (int) Math.ceil((double) b / d));
        bw.write((l - r) + "");
        bw.flush();
    }
}