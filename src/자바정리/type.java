import java.util.*;
import java.util.stream.Collectors;


public class type {

    public static void main(String[] args){

        //String[]
        String[] strArray = {"1", "2", "3", "4", "5"};

        //int[]
        int[] intArray = {1, 2, 3, 4, 5};

        // String[] -> List<String>
        ArrayList<String> stringList = new ArrayList<>(Arrays.asList(strArray));

        // List<String> -> String[] 
        String[] strArray2 = stringList.toArray(new String[0]);

        // String[] -> int[]
        int[] intArray2 = Arrays.stream(strArray)
                                .mapToInt(Integer::parseInt)
                                .toArray();

        // int[] -> String[]
        String[] strArray3 = Arrays.stream(intArray)
                                   .mapToObj(String::valueOf)
                                   .toArray(String[]::new);       

        // int[] -> List<Integer>
        List<Integer> integerList = Arrays.stream(intArray)
                                          .boxed()
                                          .collect(Collectors.toList());

        // List<Integer> -> int[]
        int[] intArray3 = integerList.stream()
                                     .mapToInt(Integer::intValue)
                                     .toArray();

        // int[] -> HashSet<Integer>
        HashSet<Integer> integerHashSet = Arrays.stream(intArray)
                                                .boxed()
                                                .collect(Collectors.toCollection(HashSet::new));
        
        // HashSet<Integer> -> int[]
        int[] intArray4 = integerHashSet.stream()
                                        .mapToInt(Integer::intValue)
                                        .toArray(); 

        //String[] -> char[]
        String joined = String.join("", strArray);
        char[] charArray = joined.toCharArray();

        //char[] -> String[]
        String[] stringArray = new String[charArray.length];
        for (int i = 0; i < charArray.length; i++) {
            stringArray[i] = String.valueOf(charArray[i]);  // 각 char를 String으로 변환
        }

        System.out.println(Arrays.toString(stringArray));
        // System.out.println(a);
    }
}
