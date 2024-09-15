import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        switch (n % 8) {
            case 0:
            case 2:
                System.out.println(2);
                break;
            case 1:
                System.out.println(1);
                break;
            case 3:
            case 7:
                System.out.println(3);
                break;
            case 4:
            case 6:
                System.out.println(4);
                break;
            default:
                System.out.println(5);
                break;
        }
    }
}