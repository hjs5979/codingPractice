import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 약수의_합_2{
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int number = Integer.parseInt(br.readLine());

        long answer = 0;

        for(int i=1; i <= number;i++){
            answer += ((number/i) * i);
        }
        System.out.print(answer);
    }
}