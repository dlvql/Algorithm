import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String ans = "";
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        if (a + b + c != 180) {
            ans = "Error";
        } else {
            if (a == b && b == c) {
                ans = "Equilateral";
            } else if (a == b || b == c || c == a) {
                ans = "Isosceles";
            } else {
                ans = "Scalene";
            }
        }
        System.out.println(ans);
    }
}