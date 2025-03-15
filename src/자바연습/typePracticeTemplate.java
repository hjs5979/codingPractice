import java.util.*;
import java.util.stream.Collectors;

public class typePracticeTemplate {
        public static void main(String[] args){

        //String[]
        String[] stringArray = {"1", "2", "3", "4", "5"};
        
        //StringList
        List<String> stringList = new ArrayList<>();
        stringList.add("1");
        stringList.add("2");
        stringList.add("3");
        stringList.add("4");
        stringList.add("5");

        //int[]
        int[] intArray = {1, 2, 3, 4, 5};
        
        //integerList
        List<Integer> integerList = new ArrayList<>();
        integerList.add(1);
        integerList.add(2);
        integerList.add(3);
        integerList.add(4);
        integerList.add(5);

        //HashSet<Integer>
        HashSet<Integer> integerHashSet = new HashSet<>();
        integerHashSet.add(1);
        integerHashSet.add(2);
        integerHashSet.add(3);
        integerHashSet.add(4);
        integerHashSet.add(5);

        //char[]
        char[] charArray = {'1', '2', '3', '4', '5'}; 

        StringBuilder[] sbArray = new StringBuilder[12];

        for(int i = 0; i < 12; i++){
            sbArray[i] = new StringBuilder();
            
            sbArray[i].append(String.format("%6s", i) +" . ");
        }

        List<String> stringListAnswer = new ArrayList<>();
        String[] stringArrayAnswer = new String[stringArray.length];
        int[] intArrayAnswer = new int[intArray.length];
        List<Integer> integerListAnswer = new ArrayList<>();
        HashSet<Integer> integerHashSetAnswer = new HashSet<>();
        char[] charArrayAnswer = new char[charArray.length];
        String stringTypeAnswer = "";
        
// ====================================================================================================================================================

        // 1. String[] -> List<String>
        // stringListAnswer =
        sbArray[1].append(stringListAnswer + "\n");

        // 2. List<String> -> String[] 
        // stringArrayAnswer = 
        sbArray[2].append(Arrays.toString(stringArrayAnswer) + "\n");

        // 3. int[] -> List<Integer>
        // integerListAnswer =
        sbArray[3].append(integerListAnswer + "\n");

        // 4. List<Integer> -> int[]
        // intArrayAnswer =
        sbArray[4].append(Arrays.toString(intArrayAnswer) + "\n");

        // 5. String[] -> int[]
        //  intArrayAnswer =
        sbArray[5].append(Arrays.toString(intArrayAnswer) + "\n");

        // 6. int[] -> String[]     
        // stringArrayAnswer =
        sbArray[6].append(Arrays.toString(stringArrayAnswer) + "\n");

        // 7. int[] -> HashSet<Integer>
        // integerHashSetAnswer =
        sbArray[7].append(integerHashSetAnswer + "\n");

        // 8. HashSet<Integer> -> int[]
        // intArrayAnswer =
        sbArray[8].append(Arrays.toString(intArrayAnswer) + "\n");
        
        // 9. String[] -> char[]
        // charArrayAnswer =
        sbArray[9].append(Arrays.toString(charArrayAnswer) + "\n");

        // 10. char[] -> String[]

        //for문 사용

        sbArray[10].append(Arrays.toString(stringArrayAnswer) + "\n");

        // 11. char[] -> String
        // stringTypeAnswer =

        sbArray[11].append(stringTypeAnswer + "\n");

// =================================================================================================================================================

        // 1번 String[] -> List<String> 정답
        ArrayList<String> number1Answer = new ArrayList<>(Arrays.asList(stringArray));
        sbArray[1].append("Answer : " + number1Answer + "\n");
        
        // 2번 List<String> -> String[] 정답
        String[] number2Answer = stringList.toArray(new String[0]);
        sbArray[2].append("Answer : " + Arrays.toString(number2Answer) + "\n");

        // 3번 int[] -> List<Integer> 정답
        List<Integer> number3Answer = Arrays.stream(intArray).boxed().collect(Collectors.toList());
        sbArray[3].append("Answer : " + number3Answer + "\n");

        // 4번 List<Integer> -> int[] 정답
        int[] number4Answer = integerList.stream().mapToInt(Integer::intValue).toArray();
        sbArray[4].append("Answer : " + Arrays.toString(number4Answer) + "\n");

        // 5번 String[] -> int[] 정답
        int[] number5Answer = Arrays.stream(stringArray).mapToInt(Integer::parseInt).toArray();
        sbArray[5].append("Answer : " + Arrays.toString(number5Answer) + "\n");

        // 6번 int[] -> String[] 정답
        String[] number6Answer = Arrays.stream(intArray).mapToObj(String::valueOf).toArray(String[]::new);
        sbArray[6].append("Answer : " + Arrays.toString(number6Answer) + "\n");

        // 7번 int[] -> HashSet<Integer> 정답
        HashSet<Integer> number7Answer = Arrays.stream(intArray).boxed().collect(Collectors.toCollection(HashSet::new));
        sbArray[7].append("Answer : " + number7Answer + "\n");

        // 8번 HashSet<Integer> -> int[] 정답
        int[] number8Answer = integerHashSet.stream().mapToInt(Integer::intValue).toArray(); 
        sbArray[8].append("Answer : " + Arrays.toString(number8Answer) + "\n");

        // 9번 String[] -> char[] 정답
        char[] number9Answer = String.join("", stringArray).toCharArray();
        sbArray[9].append("Answer : " + Arrays.toString(number9Answer) + "\n");

        // 10번 char[] -> String[] 정답
        String[] number10Answer = new String[5];
        for (int i = 0; i < charArray.length; i++) {
            number10Answer[i] = String.valueOf(charArray[i]);  // 각 char를 String으로 변환
        }
        sbArray[10].append("Answer : " + Arrays.toString(number10Answer));

        // 11번 char[] -> String 정답
        String number11Answer = String.valueOf(charArray);
        sbArray[11].append("Answer : " + number11Answer);
// =========================================================================================================================================

        for(int i = 1; i < 12; i++){
            System.out.println(sbArray[i]);
        }


    }
}
