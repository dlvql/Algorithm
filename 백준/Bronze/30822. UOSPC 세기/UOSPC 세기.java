import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        char[] s = sc.next().toCharArray();
        int[] uospc = new int[5];
        int m = 1000;
        for (char c: s) {
            if (c == 'u') uospc[0]++;
            else if (c == 'o') uospc[1]++;
            else if (c == 's') uospc[2]++;
            else if (c == 'p') uospc[3]++;
            else if (c == 'c') uospc[4]++;
        }
        for (int i: uospc) {
            if (i < m) m = i;
        }
        System.out.println(m);
    }
}