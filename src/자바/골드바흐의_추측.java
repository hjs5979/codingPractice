import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.Arrays;

class 골드바흐의_추측{
    public static void main(String args[]) throws IOException{
        int n = 1000001;

        boolean[] primeBooleanArray = new boolean[n];

        primeBooleanArray[0] = true;
        primeBooleanArray[1] = true;

        for(int i = 3;i<Math.sqrt(n)+1;i=i+2 ){
            if (!primeBooleanArray[i]){
                for (int j=2*i;j<n;j=j+i){
                    primeBooleanArray[j] = true;
                }
            }
        }

        // System.out.println(Arrays.toString(primeBooleanArray));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        while(true){
            int a = Integer.parseInt(br.readLine());
            
            if (a == 0){
                break;
            }
            for (int i=3; i < (a/2)+1 ;i=i+2){
                if(!primeBooleanArray[i] && !primeBooleanArray[a-i]){
                    System.out.println(a + " = " + i + " + " + (a-i));
                    break;
                }
            }
        }
    } 
}