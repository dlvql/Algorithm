import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double score_sum = 0;
        double score_gpa = 0;
        for (int i = 0; i < 20; i++){
            String[] str = sc.nextLine().split(" ");
            double scr = Double.parseDouble(str[1]);

            char[] gpa = str[2].toCharArray();
            double scp = 0;
            switch (gpa[0]) {
                case 'P':
                    scr = 0;
                    break;
                case 'A':
                    scp += 4;
                    break;
                case 'B':
                    scp += 3;
                    break;
                case 'C':
                    scp += 2;
                    break;
                case 'D':
                    scp += 1;
                    break;
                case 'F':
                    break;
            }
            if (gpa.length > 1 && gpa[1] == '+'){
                scp += 0.5;
            }
            score_sum += scr;
            score_gpa += scp * scr;
        }
        System.out.println(score_gpa / score_sum);
    }
}