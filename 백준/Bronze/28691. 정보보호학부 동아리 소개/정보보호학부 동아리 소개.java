import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s = br.readLine();
        if (s.equals("M")) bw.write("MatKor");
        else if (s.equals("W")) bw.write("WiCys");
        else if (s.equals("C")) bw.write("CyKor");
        else if (s.equals("A")) bw.write("AlKor");
        else if (s.equals("$")) bw.write("$clear");
        bw.flush();
    }
}