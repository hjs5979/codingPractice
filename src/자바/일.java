import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class 일{

    public static int check(int n){
        
        int ones = 0;
        int answer = 1;

        while(true){
            ones = ones * 10 + 1;
            if (ones % n == 0){
                break;
            }
            else{
                answer += 1;
                ones = ones%n;
            }
        }
        return answer;
    }
    
    public static void main(String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        while(true){
            String s = br.readLine();
            if (s==null){
                break;
            }
            int number = Integer.parseInt(s);
            int ans = check(number);
            System.out.println(ans);
            }
        br.close();
        }
    }