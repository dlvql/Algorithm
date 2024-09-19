import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            String s = sc.next();
            int l = (int) Math.sqrt(s.length());
            char[][] encode = new char[l][l];
            for (int j = 0, idx = 0; j < l; j++) {
                for (int k = 0; k < l; k++) {
                    encode[j][k] = s.charAt(idx);
                    idx++;
                }
            }
            for (int j = l - 1; j >= 0; j--) {
                for (int k = 0; k < l; k++) {
                    System.out.print(encode[k][j]);
                }
            }
            System.out.println();
        }
    }
}