import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] n = sc.next().toCharArray();
        int b = sc.nextInt();
        int ans = 0;
        for (int i = 0, j = n.length - 1; i < n.length; i++, j--) {
            int now = n[i] >= 'A' ? n[i] - 'A' + 10 : n[i] - 48;
            ans += (int) Math.pow(b, j) * now;
        }
        System.out.println(ans);
    }
}