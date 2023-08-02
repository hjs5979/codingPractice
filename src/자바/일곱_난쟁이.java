import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

class 일곱_난쟁이{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int[] heightArray = new int[9];
        int sum = 0;
        int index1 = 0;
        int index2 = 0;

        for(int i=0;i<9;i++){
            heightArray[i] = Integer.parseInt(br.readLine());
            sum += heightArray[i];
        }
        Arrays.sort(heightArray);
        Loop1:
        for (int i=0;i<9;i++){
            Loop2:
            for(int j=i+1;j<9;j++){
                if ((sum - heightArray[i] - heightArray[j]) == 100){
                    index1 = i;
                    index2 = j;
                    break Loop1;  
                }
            }
        }

        for (int i=0;i<9;i++){
            if ((i != index1) && (i!= index2)){
                System.out.println(heightArray[i]);
            }
        }
    }
}