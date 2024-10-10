class Solution {
    public int solution(int a, int b, int n) {
        int cnt = 0;
        int now = n, less = 0;
        while (now >= a) {
            less = now % a;
            now -= less;
            now = (now / a) * b;
            cnt += now;
            now += less;
        }
        return cnt;
    }
}