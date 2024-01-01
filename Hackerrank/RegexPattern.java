import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class RegexPattern {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        scan.nextLine();
        for (int i = 0; i < N; i++) {

            String Name = scan.nextLine();
            String regex = "^[a-zA-Z][a-zA-Z0-9_]{7,29}";
            Pattern pattern = Pattern.compile(regex);

            Matcher matcher = pattern.matcher(Name);
            boolean matchFound = matcher.matches();

            if (matchFound) {
                System.out.println("Match found");
            } else {
                System.out.println("Match not found");
            }
        }

        scan.close();

    }
}
