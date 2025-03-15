import java.util.*;

public class permutation_string{
    
    public static ArrayList<String> combinationsList = new ArrayList<>();

    public static void combi(int idx, char[] chars, String result){
        
        if(result.length() > 0){
            combinationsList.add(result);
        }

        for(int i = idx; i < chars.length; i++){
            combi(i+1, chars, result + chars[i]);
        }

    }
    
    public static void main(String[] args){
        
        char[] input = new char[]{'A', 'B', 'C'};

        combi(0, input, "");

        System.out.println(combinationsList);

    }
}