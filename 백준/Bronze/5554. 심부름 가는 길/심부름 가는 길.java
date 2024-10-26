import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int s = 0;
        for (int i = 0; i < 4; i++) s += Integer.parseInt(br.readLine());
        bw.write((s / 60) + "\n" + s % 60);
        bw.flush();
    }
}