import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLine()) {
            String s = sc.nextLine();
            while (s.contains("BUG")) {
                s = s.replace("BUG", "");
            }
            bw.write(s + "\n");
        }
        bw.flush();
    }
}