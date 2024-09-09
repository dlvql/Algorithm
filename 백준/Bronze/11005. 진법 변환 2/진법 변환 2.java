import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int b = sc.nextInt();
        String s = "";
        while (n >= b) {
            char c = (char) ((n % b) >= 10 ? (n % b) + 'A' - 10 : (n % b) + '0');
            s = c + s;
            n /= b;
        }
        System.out.println((char) (n >= 10 ? (n + 'A' - 10) : (n + '0')) + s);
    }
}