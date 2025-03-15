import java.util.*;
import java.util.stream.Collectors;

public class hashMap{

   public static void main(String[] args){

      HashMap<Integer, ArrayList<String>> hashMap = new HashMap<>();

      String[] stringArray = {"1", "2", "3"};

      //Map 데이터 넣는법
      for(int i = 0; i < 3; i++){
         hashMap.put(i, new ArrayList<>(Arrays.asList(stringArray)));   
      }
      
      // 2. for/foreach으로 모든 map을 출력하라.
      //Map의 for문 사용법
      for (Map.Entry<Integer, ArrayList<String>> entry : hashMap.entrySet()) {
         System.out.println("[key]:" + entry.getKey() + ", [value]:" + entry.getValue());
      }

       //Map의 forEach 사용법
       hashMap.forEach((key, value) -> {
         System.out.println("[key]:" + key + ", [value]:" + value);
      });

      // 3. key 존재여부 확인법 / key 없으면 디폴트값으로 get
      
      System.out.println(hashMap.containsKey(0));

      System.out.println(hashMap.getOrDefault(4, new ArrayList<>()));

      HashMap<Integer, Integer> hashMap2 = new HashMap<>();

      hashMap2.put(1, 3);
      hashMap2.put(2, 2);
      hashMap2.put(3, 1);

      //Map의 stream 사용법
      hashMap2.entrySet().stream()
            .forEach(
               entry-> { 
                  System.out.println("[key]:" + entry.getKey() + ", [value]:"+entry.getValue());
               }
            );
      
      //정렬(key)
      hashMap2.entrySet().stream()
            .sorted(
               Map.Entry.comparingByKey()
            )
            .forEach(
               entry-> {
                     System.out.println("[key]:" + entry.getKey() + ", [value]:"+entry.getValue());
               }
            );

      //정렬(value)
      hashMap2.entrySet().stream()
            .sorted(
               Map.Entry.comparingByValue()
            )
            .forEach(
               entry-> {
                  System.out.println("[key]:" + entry.getKey() + ", [value]:"+entry.getValue());
               }
            );

      //정렬(내림차순)
      hashMap.entrySet().stream()
            .sorted(
               Map.Entry.comparingByKey(Comparator.reverseOrder())
            )
            .forEach(
               entry-> {
                  System.out.println("[key]:" + entry.getKey() + ", [value]:"+entry.getValue());
               }
            );

      // 최대값 찾기
      // max 같은 경우 값이 없을 때, 값을 지정시켜줘야함 ex) orElse
      
      int max1 = hashMap2.values().stream().max(Comparator.comparingInt(value -> value)).orElse(-1);
        
      int max2 = hashMap2.values().stream().max(Integer::compare).orElse(-1);

      int max3 = hashMap2.values().stream().max((x,y) -> x - y).orElse(-1);
      
      // for문으로 Map을 돌면서 최댓값 value찾고 그 value의 key도 찾기
      int maxValue = 0;
      int maxKey = 0;
      for (Map.Entry<Integer, Integer> entry : hashMap2.entrySet()) {
         if (entry.getValue() > maxValue) {
             maxValue = entry.getValue();
         }
      }
      System.out.println("[maxKey]:" + maxKey + ", [maxValue]:" + maxValue);

      // filter 거는법
      Map<Integer, Integer> filteredMap = hashMap2.entrySet().stream().filter(entry -> entry.getValue() > 1).collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
                                                  
        
    }
}