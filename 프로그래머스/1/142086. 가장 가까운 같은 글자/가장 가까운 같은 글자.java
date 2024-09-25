class Solution {
    public int[] solution(String str) {
        char[] s = str.toCharArray();
        int[] apb = new int[26];
        int[] ans = new int[s.length];
        for (int i = 0; i < s.length; i++) {
            if(apb[s[i] - 'a'] == 0) ans[i] = -1;
            else ans[i] = i + 1 - apb[s[i] - 'a'];
            apb[s[i] - 'a'] = i + 1;
        }
        return ans;
    }
}