import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            String y = br.readLine();
            int np = Integer.parseInt(y) + 1;
            if (np % Integer.parseInt(y.substring(y.length() - 2)) == 0) {
                bw.write("Good\n");
            } else {
                bw.write("Bye\n");
            }
        }
        bw.flush();
    }
}