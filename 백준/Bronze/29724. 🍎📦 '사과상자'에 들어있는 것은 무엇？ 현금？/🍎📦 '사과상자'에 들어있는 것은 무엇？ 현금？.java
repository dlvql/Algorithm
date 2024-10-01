import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int s = 0;
        int c = 0;
        for (int i = 0 ; i < n; i++) {
            String[] r = br.readLine().split(" ");
            char t = r[0].charAt(0);
            int w = (int) Math.floor((double) Integer.parseInt(r[1]) / 12);
            int h = (int) Math.floor((double) Integer.parseInt(r[2]) / 12);
            int l = (int) Math.floor((double) Integer.parseInt(r[3]) / 12);
            if (t == 'A') {
                s += 1000 + (w * h * l * 500);
                c += w * h * l;
            } else {
                s += 50 * 120;
            }
        }
        System.out.println(s);
        System.out.println(c * 4000);
    }
}
