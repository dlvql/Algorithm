import java.util.Arrays;

class Solution {
    public int[] solution(int[] numbers) {
        int l = numbers.length;
        int[] arr = new int[201];
        int[] ans = new int[201];
        Arrays.fill(arr, -1);
        Arrays.fill(ans, -1);
        for (int i = 0; i < l; i++) {
            for (int j = i + 1; j < l; j++) {
                arr[numbers[i] + numbers[j]] = 1;
            }
        }
        for (int i = 0; i < 201; i++) {
            if (arr[i] != -1) ans[i] = i;
        }
        return Arrays.stream(ans).filter(i -> i != -1).toArray();
    }
}