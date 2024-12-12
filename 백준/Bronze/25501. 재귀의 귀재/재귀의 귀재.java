import java.io.*;

public class Main {
    public static String recursion(String s, int l, int r, int c){
        if(l >= r) return ("1 " + c);
        else if(s.charAt(l) != s.charAt(r)) return ("0 " + c);
        else return recursion(s, l+1, r-1, c + 1);
    }
    public static String isPalindrome(String s, int c){
        return recursion(s, 0, s.length()-1, c);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            int c = 1;
            bw.write(isPalindrome(s, c) + "\n");
        }
        bw.flush();
    }
}