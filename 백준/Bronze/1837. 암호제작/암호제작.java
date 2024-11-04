import java.math.BigInteger;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] arr = br.readLine().split(" ");
        BigInteger a = new BigInteger(arr[0]);
        BigInteger k = new BigInteger(arr[1]);
        boolean isBad = false;
        for (BigInteger i = new BigInteger("2"); i.compareTo(k) < 0; i = i.add(BigInteger.ONE)) {
            if (a.mod(i).equals(BigInteger.ZERO)) {
                bw.write("BAD " + i);
                isBad = true;
                break;
            }
        }
        if (!isBad) bw.write("GOOD");
        bw.flush();
    }
}