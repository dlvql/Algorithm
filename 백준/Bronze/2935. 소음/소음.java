import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String n = br.readLine();
        String s = br.readLine();
        String m = br.readLine();
        if (s.equals("+")) {
            if (n.length() == m.length()) {
                bw.write("2");
                for (int i = 0; i < n.length() - 1; i++) bw.write("0");
            } else {
                bw.write("1");
                if (n.length() > m.length()) {
                    for (int i = 0; i < n.length() - 1 - m.length(); i++) bw.write("0");
                    bw.write(m + "");
                } else {
                    for (int i = 0; i < m.length() - 1 - n.length(); i++) bw.write("0");
                    bw.write(n + "");
                }
            }
        }
        else {
            bw.write("1");
            for (int i = 0; i < n.length() + m.length() - 2; i++) {
                bw.write("0");
            }
        }
        bw.flush();
    }
}