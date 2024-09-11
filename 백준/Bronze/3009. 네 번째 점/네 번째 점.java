import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x1 = sc.nextInt(), y1 = sc.nextInt();
        int x2 = sc.nextInt(), y2 = sc.nextInt();
        int x3 = sc.nextInt(), y3 = sc.nextInt();
        if (x1 == x2) System.out.print(x3 + " ");
        else if (x1 == x3)  System.out.print(x2 + " ");
        else System.out.print(x1 + " ");
        if (y1 == y2) System.out.println(y3);
        else if (y1 == y3)  System.out.println(y2);
        else System.out.println(y1);
    }
}