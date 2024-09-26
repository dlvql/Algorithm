import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        long sum = 0;
        long[] prices = new long[n];
        for (int i = 0; i < n; i++) {
            prices[i] = Long.parseLong(br.readLine());
        }

        Arrays.sort(prices);

        for (int i = n - 1; i >= 2; i -= 3) {
            sum += prices[i] + prices[i - 1];
        }

        for (int i = 0; i < n % 3; i++) {
            sum += prices[i];
        }

        System.out.println(sum);
    }
}