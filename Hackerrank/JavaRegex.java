import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class JavaRegex {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        scan.nextLine();
        for (int i = 0; i < N; i++) {

            String Name = scan.nextLine();
            String regex = "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?(\\.|$)){4}";
            Pattern pattern = Pattern.compile(regex);

            Matcher matcher = pattern.matcher(Name);
            boolean matchFound = matcher.find();

            if (matchFound) {
                System.out.println("Match found");
            } else {
                System.out.println("Match not found");
            }
        }

        scan.close();
    }
}
