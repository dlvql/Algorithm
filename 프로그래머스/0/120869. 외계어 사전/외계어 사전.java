class Solution {
    public int solution(String[] spell, String[] dic) {
        int isExist = 2;
        for (String n: dic) {
            int cnt = 0;
            for (String c: spell) {
                if (n.contains(c)) {
                    cnt += 1;
                }
            }
            if (cnt == n.length() && cnt == spell.length) {
                isExist = 1;
                break;
            }
        }
        return isExist;
    }
}