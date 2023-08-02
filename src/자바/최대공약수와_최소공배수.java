import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 최대공약수와_최소공배수{
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        int min_value = Math.min(a, b);

        int max_value = 0;

        for(int i = 1; i < min_value+1; i++){
            if (a%i==0 && b%i==0 && max_value < i){
                max_value = i;
            }
        
        }
        System.out.println(max_value);
        System.out.println(max_value * (a/max_value) * (b/max_value));
        
    }
}