import java.util.*;
import java.util.stream.Collectors;

public class hashMapTemplate{

   public static void main(String[] args){

      HashMap<String, Integer> hashMap = new HashMap<>();

      hashMap.put("b", 3);
      hashMap.put("d", 4);
      hashMap.put("c", 2);
      hashMap.put("a", 1);

      int max = 0;
      int maxValue = 0;
      String maxKey = "";

      // 1. stream으로 최대값 찾기
      max = hashMap.values().stream().max(Integer::compare).orElse(-1);

      // 2. for문으로 Map을 돌면서 최댓값 value찾고 그 value의 key도 찾기
      
      for (Map.Entry<String, Integer> entry : hashMap.entrySet()) {
         if (entry.getValue() > maxValue) {
             maxValue = entry.getValue();
             maxKey = entry.getKey();
         }
      }

      // 3. stream으로 filter맵 생성
      Map<String, Integer> filteredMap = hashMap.entrySet().stream().filter(entry -> entry.getValue() > 1).collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
      
      // 4. for문으로 filter맵 생성
      Map<String, Integer> filteredMap2 = new HashMap<>();
      for (Map.Entry<String, Integer> entry : hashMap.entrySet()) {
         if (entry.getValue() > 1) { // 조건: 값이 1보다 큰 경우
            filteredMap2.put(entry.getKey(), entry.getValue());
      }
}      
// ==============================================================================================================================================

      System.out.println("number1 : " + max);
      System.out.println(" Answer : " + 4);

      System.out.println();

      System.out.println("number2 : key-" + maxKey + " value-" + maxValue);
      System.out.println(" Answer : key-" + maxKey + " value-" + maxValue);

      System.out.println();

      System.out.println("number3");

      filteredMap.forEach((key, value) -> {
            System.out.println("key : " + key + " " + "value : " + value);
         }
      );
      
      System.out.println();

      System.out.println("number4");

      filteredMap2.forEach((key, value) -> {
            System.out.println("key : " + key + " " + "value : " + value);
         }
      );
      
    }
}