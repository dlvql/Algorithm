import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] p = br.readLine().split(" ");
        StringBuilder sb = new StringBuilder();
        String[] np = new String[9];
        for (int i = 0; i < 9; i++) {
            np[Integer.parseInt(p[i]) - 1] = String.valueOf(i + 1);
        }
        HashMap<Character, String> hash = new HashMap<>();
        for (int i = 0, j = 1; i < 26; i += 3, j++) {
            int asc = i + 97;
            hash.put((char) asc, np[j]);
            hash.put((char) (asc + 1), np[j] + np[j]);
            hash.put((char) (asc + 2), np[j] + np[j] + np[j]);
            if ((asc == 112) || (asc == 119)) {
                hash.put((char) (asc + 3), np[j] + np[j] + np[j] + np[j]);
                i ++;
            }
        }
        char[] arr = br.readLine().toCharArray();
        for (char n: arr) {
            String add = hash.get(n);
            if (!sb.toString().isEmpty() && sb.charAt(sb.length() - 1) == add.charAt(0)) {
                sb.append("#");
            }
            sb.append(add);
        }
        bw.write(sb.toString());
        bw.flush();
    }
}