import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int max = -1000000;// -1,000,000
        int min = 1000000;
        for(int i = 0; i < n; i++) {
            int a = sc.nextInt();
            if(a > max) max = a;
            if(a < min) min = a;
        }
        System.out.println(min + " " + max);
    }
}