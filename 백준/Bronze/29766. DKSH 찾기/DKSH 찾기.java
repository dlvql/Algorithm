import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int l = s.length();
        s = s.replace("DKSH", "");
        System.out.println((l - s.length()) / 4);
    }
}