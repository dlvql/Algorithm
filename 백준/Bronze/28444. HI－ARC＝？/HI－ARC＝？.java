import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        // H * I - A * R * C
        String[] arr = br.readLine().split(" ");
        int[] hiarc = new int[5];
        for(int i = 0; i < 5; i++) hiarc[i] = Integer.parseInt(arr[i]);
        bw.write(((hiarc[0] * hiarc[1]) - (hiarc[2] * hiarc[3] * hiarc[4])) + "");
        bw.flush();
    }
}