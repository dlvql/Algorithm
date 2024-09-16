import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong(), m = sc.nextLong();
        if ((n - 1) % (m + 1) == 0) System.out.println("Can't win");
        else System.out.println("Can win");
    }
}