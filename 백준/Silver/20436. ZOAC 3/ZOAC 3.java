import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = 0;
        String isLeft = "qwertasdfgzxcv";
        HashMap<Character, int[]> key = new HashMap<>();
        key.put('q', new int[]{0, 0});
        key.put('w', new int[]{0, 1});
        key.put('e', new int[]{0, 2});
        key.put('r', new int[]{0, 3});
        key.put('t', new int[]{0, 4});
        key.put('y', new int[]{0, 5});
        key.put('u', new int[]{0, 6});
        key.put('i', new int[]{0, 7});
        key.put('o', new int[]{0, 8});
        key.put('p', new int[]{0, 9});
        key.put('a', new int[]{1, 0});
        key.put('s', new int[]{1, 1});
        key.put('d', new int[]{1, 2});
        key.put('f', new int[]{1, 3});
        key.put('g', new int[]{1, 4});
        key.put('h', new int[]{1, 5});
        key.put('j', new int[]{1, 6});
        key.put('k', new int[]{1, 7});
        key.put('l', new int[]{1, 8});
        key.put('z', new int[]{2, 0});
        key.put('x', new int[]{2, 1});
        key.put('c', new int[]{2, 2});
        key.put('v', new int[]{2, 3});
        key.put('b', new int[]{2, 4});
        key.put('n', new int[]{2, 5});
        key.put('m', new int[]{2, 6});
        String f = br.readLine();
        int[] l = key.get(f.charAt(0)), r = key.get(f.charAt(2));
        String s = br.readLine();
        for (char c: s.toCharArray()) {
            boolean isContainsInLeft = isLeft.contains(String.valueOf(c));
            int[] xy = key.get(c);
            if (isContainsInLeft) {
                t += Math.abs(xy[0] - l[0]) + Math.abs(xy[1] - l[1]) + 1;
                l = xy;
            } else {
                t += Math.abs(xy[0] - r[0]) + Math.abs(xy[1] - r[1]) + 1;
                r = xy;
            }
        }
        bw.write(t + "");
        bw.flush();
    }
}