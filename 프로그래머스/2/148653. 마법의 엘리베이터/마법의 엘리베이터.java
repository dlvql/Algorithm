import java.util.*;

class Solution {
    public int solution(int storey) {
        int s = 0;
        while (storey >= 6) {
            int now = storey % 10;
            int next = (storey / 10) % 10;
            if (now >= 6 || (now == 5 && next >= 5)) {
                storey += 10 - now;
                s += 10 - now;
            } else {
                storey -= now;
                s += now;
            }
            storey /= 10;
        }
        return s + storey;
    }
}