import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] a = Arrays.stream(br.readLine().split(" "))
                        .mapToInt(Integer::parseInt)
                        .toArray();
        int[] b = Arrays.stream(br.readLine().split(" "))
                        .mapToInt(Integer::parseInt)
                        .toArray();
        int asc = 0, bsc = 0, lstW = -1;
        for (int i = 0; i < 10; i++) {
            if(a[i] > b[i]) {
                asc += 3;
                lstW = 0;
            } else if (b[i] > a[i]) {
                bsc += 3;
                lstW = 1;
            } else {
                asc += 1;
                bsc += 1;
            }
        }
        bw.write(asc + " " + bsc + "\n");
        if (asc == bsc && asc == 10) {
            bw.write("D");
        } else if (asc == bsc) {
            bw.write(lstW == 0 ? "A" : "B");
        } else {
            bw.write(asc > bsc ? "A" : "B");
        }
        bw.flush();
    }
}