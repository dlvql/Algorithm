import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine()), cnt = 0, a = 0, nr = 0;
        while (cnt < n) {
            String arr = br.readLine();
            if (arr.isEmpty()) {
                String per = String.format("%.1f", ((double)(a - nr) / a) * 100);
                if (per.charAt(per.length() - 1) == '0') {
                    per = String.valueOf(Math.round(Double.parseDouble(per)));
                }
                bw.write("Efficiency ratio is " + per + "%.\n");
                cnt += 1;
                a = 0;
                nr = 0;
            } else {
                a += arr.length();
                for (char c : arr.toCharArray()) {
                    if (c == '#') nr++;
                }
            }
        }
        bw.flush();
    }
}