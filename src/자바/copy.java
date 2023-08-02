import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class copy{

    public static int check(int n){
        // boolean ret = false;
        
        int ones = 0;
        int answer = 1;

        while(true){
            ones = ones * 10 + 1;
            if (ones % n == 0){
                // ret = true;
                break;
            }
            else{
                answer += 1;
            }
        }
        return answer;
    }
    
    public static void main(String[] args){

        while(true){
            try{
                BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
                int number = Integer.parseInt(br.readLine());
                int ans = check(number);
                System.out.println(ans);
            }
            catch(Exception e){
                break;
            }
        }
    }
}