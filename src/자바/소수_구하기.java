import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 소수_구하기{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        boolean[] p_list = new boolean[b+1];

        p_list[0] = true;
        p_list[1] = true;

        for (int i =0;i<Math.sqrt(b)+1;i++){
            if(p_list[i]==true){
                continue;
            }
            for (int j=i*i;j<b+1;j=j+i){
                p_list[j] = true;
            }
        }
        
        for (int i=a;i <= b;i++){
            if (p_list[i] == false){
                System.out.println(i);
            }
        }
        
    }
        
}