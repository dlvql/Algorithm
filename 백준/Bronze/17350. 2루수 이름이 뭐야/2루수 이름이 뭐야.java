import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write("뭐야");
        int n = Integer.parseInt(br.readLine());
        boolean isEqual = false;
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            if (s.equals("anj")) {
                isEqual = true;
                break;
            }
        }
        if (isEqual) bw.write(";");
        else bw.write("?");
        bw.flush();
    }
}