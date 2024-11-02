import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder[] arr = Arrays.stream(br.readLine().split(" ")).map(e -> new StringBuilder(e)).toArray(StringBuilder[]::new);
        int rvsum = Integer.parseInt(String.valueOf(arr[0].reverse())) + Integer.parseInt(String.valueOf(arr[1].reverse()));
        bw.write(String.valueOf(Integer.parseInt(String.valueOf(new StringBuilder(String.valueOf(rvsum)).reverse()))));
        bw.flush();
    }
}