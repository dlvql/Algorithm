import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] str = sc.nextLine().strip().split(" ");
        int cnt = 0;
        for (String s : str) {
            if (s == "") continue;
            cnt ++;
        }
        System.out.println(cnt);
    }
}