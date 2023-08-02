import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 소수_찾기{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String s = br.readLine();

        String c = br.readLine();

        String[] a= c.split(" ");

        boolean[] p = new boolean[1001];

        p[0] = true;
        p[1] = true;

        for (int i =2;i<Math.sqrt(1001);i++){
            if (p[i] == true){
                continue;
            }
            for(int j=i*i;j<1001;j=j+i){
                p[j] = true;
            }

            
        }
    int answer = 0 ;

    for (String i : a){
        int index = Integer.parseInt(i);
        if (p[index]==false){
            answer+=1;
        }
    }

    System.out.println(answer);

    }
}