import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String ans = "";
        Arrays.sort(participant);
        Arrays.sort(completion);
        for (int i = 0; i < completion.length; i++) {
            if (!participant[i].equals(completion[i])) {
                ans = participant[i];
                break;
            }
        }
        if (ans.equals("")) {
            ans = participant[participant.length - 1];
        }
        return ans;
    }
}