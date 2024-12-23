import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] now = br.readLine().split("-");
        int[] date = new int[3];
        int cnt = 0;
        for (int i = 0; i < 3; i++) date[i] = Integer.parseInt(now[i]);
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String[] temp = br.readLine().split("-");
            if (Integer.parseInt(temp[0]) == date[0]) {
                if (Integer.parseInt(temp[1]) == date[1]) {
                    if (Integer.parseInt(temp[2]) >= date[2]) cnt++;
                } else if (Integer.parseInt(temp[1]) > date[1]) cnt++;
            }
            else if (Integer.parseInt(temp[0]) > date[0]) cnt++;
        }
        bw.write(cnt + "");
        bw.flush();
    }
}