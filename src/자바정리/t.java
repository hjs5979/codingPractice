import java.util.*;

class t {

    public static HashMap<String, String> linkMap = new HashMap<>();
    
    public static HashMap<String, Integer> moneyMap = new HashMap<>();

    public static int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        
        for(int i = 0; i < enroll.length; i++){
            linkMap.put(enroll[i], referral[i]);
            moneyMap.put(enroll[i], 0);
            moneyMap.put("-", 0);
        }
        
        for(int i = 0; i < seller.length ; i++){
            String link = seller[i];
            //String link = linkMap.get(seller[i]);
            Integer amnt = amount[i] * 100;

            while(!(link.equals("-"))){
                Integer dValue = amnt / 10;
                
                Integer value = amnt - dValue;

                moneyMap.put(link, moneyMap.get(link) + value);
                
                link = linkMap.get(link);
                amnt = dValue;
            }

            

        }
        ArrayList<Integer> answer = new ArrayList<>();

        for(int i = 0; i < enroll.length ; i++){
            answer.add(moneyMap.get(enroll[i]));
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();        
    }

    public static void main(String[] args){
        String[] enroll = new String[] {"john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"};	
        String[] referral = new String[] {"-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"};
        String[] seller = new String[] {"young", "john", "tod", "emily", "mary"};
        int[] amount = new int[] {12, 4, 2, 5, 10};

        int[] answer = solution(enroll, referral, seller, amount);

        System.out.println(answer);
        
    }
}
