import java.util.*;
import java.util.stream.Collectors;

public class dataStructure {

    private static class Node{
        int first, second;
  
        public Node(int first, int second){
            this.first = first;
            this.second = second;
        }
  
    }

    public static void main(String[] args){

        StringBuilder[] sbArray = new StringBuilder[12];

        for(int i = 0; i < 12; i++){
            sbArray[i] = new StringBuilder();
        }

        //스택 ======================================================================================================================================================================================================================================================
        Stack<Integer> stack = new Stack<>();
        
        //스택 : 뒤로 삽입
        stack.push(1);
        stack.push(2);
        stack.push(3);

        //스택 : 맨 뒤의 값 반환
        int stackValue1 = stack.peek();

        //스택 : 맨 뒤의 값 반환하고 삭제
        int stackValue2 = stack.pop();

        //큐 ======================================================================================================================================================================================================================================================
        Queue<Integer> queue = new ArrayDeque<>();

        //큐 : 뒤로 삽입
        queue.add(1);
        queue.add(2);
        queue.add(3);

        //큐 : 맨 앞의 값 반환
        int queueValue1 = queue.peek();

        //큐 : 맨 앞의 값 반환하고 삭제
        int queueValue2 = queue.poll();

        //데크 ======================================================================================================================================================================================================================================================
        ArrayDeque<Integer> deque = new ArrayDeque<>();
        
        //데크 : 뒤로 삽입
        deque.add(1);

        //데크 : 뒤로 삽입
        deque.addLast(2);

        //데크 : 앞으로 삽입
        deque.addFirst(3);
        
        //그대로 뒤로 삽입 - collection 타입(List : stack, ArrayList, queue, deque / Set : HashSet 등) 
        deque.addAll(stack);

        //맨 앞의 값 반환
        int dequeValue1 = deque.peek();
        int dequeValue2 = deque.peekFirst();
        int dequeValue3 = deque.getFirst();

        //맨 앞의 값 반환하고 삭제
        int dequeValue4 = deque.poll();
        int dequeValue5 = deque.pollFirst();

        //맨 뒤의 값 반환
        int dequeValue6 = deque.peekLast();
        int dequeValue7 = deque.getLast();

        //맨 뒤의 값 반환하고 삭제
        int dequeValue8 = deque.pollLast();

        // Priority Queue ===================================================================================================================================================================================================================================

        //우선순위 큐 : 오름차순으로 정렬됨
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        pq.add(1);
        pq.add(2);
        pq.add(3);

        // 우선순위 큐 : 내림차순
        PriorityQueue<Integer> pq2 = new PriorityQueue<>(Collections.reverseOrder());

        pq2.add(1);
        pq2.add(2);
        pq2.add(3);

        //Array ======================================================================================================================================================================================================================================================
        int[] array = {1, 2, 3, 4, 5};
        
        //배열 길이
        int l = array.length;

        //배열 오름차순 정렬
        Arrays.sort(array);

        //배열 0으로 채우기
        // Arrays.fill(array, 0);

        // 최대값
        int maxValue = Arrays.stream(array).max().getAsInt();

        // 최소값
        int minValue = Arrays.stream(array).min().getAsInt();

        //Array[][] ======================================================================================================================================================================================================================================================

        int[][] array2 = {{1,2}, {3,4}, {5,6}};

        // 첫 번째 요소를 기준으로 오름차순 정렬
        Arrays.sort(array2, (o1, o2) -> Integer.compare(o1[0], o2[0]));

        //첫 번째 요소를 기준으로 내림차순 정렬
        Arrays.sort(array2, (o1, o2) -> Integer.compare(-o1[0], -o2[0]));

        //두 번째 요소를 기준으로 내림차순 정렬
        Arrays.sort(array2, (o1, o2) -> Integer.compare(o1[1], o2[1]));

        //두 번째 요소를 기준으로 내림차순 정렬
        Arrays.sort(array2, (o1, o2) -> Integer.compare(-o1[1], -o2[1]));

        //2차원 배열 출력
        System.out.println("2차원 배열 : " + Arrays.deepToString(array2));

        //ArrayList ======================================================================================================================================================================================================================================================
        ArrayList<Integer> arrayList = new ArrayList<>();
        arrayList.add(1);
        arrayList.add(2);
        arrayList.add(3);

        //리스트 인덱스 값 추출
        int listIndexValue = arrayList.get(0);

        //인덱스로 리스트 값 변경
        arrayList.set(0, 0);

        //ArrayList 두개 합칠때 사용
        arrayList.addAll(arrayList);
        System.out.println("ArrayList 두개 합칠때 사용 : " + arrayList);

        //전부 삭제
        //arrayList.clear();

        //원소 포함 여부 확인
        boolean listYn1 = arrayList.contains(1);
        System.out.println("ArrayList 원소 포함 여부 : " + listYn1);

        //ArrayList끼리 비교해서 포함 여부 확인
        boolean listYn2 = arrayList.containsAll(arrayList);
        System.out.println("ArrayList끼리 비교해서 포함 여부 확인 : " + listYn2);

        //값으로 인덱스 추출
        int listIndex = arrayList.indexOf(0);
        System.out.println("ArrayList 값으로 인덱스 추출" + listIndex);

        //비어있는지 확인
        boolean listYn3 = arrayList.isEmpty();
        System.out.println("ArrayList 비어있는지 확인 : " + listYn3);

        //forEach 사용법
        arrayList.forEach(o1 -> System.out.println("ArrayList forEach 사용법 : " + o1));

        // 값이 나오는 마지막 인덱스
        int listValue1 = arrayList.lastIndexOf(3);
        System.out.println("ArrayList 값이 나오는 마지막 인덱스 : " + listValue1);

        //인덱스의 값을 제거
        arrayList.remove(0);

        //모든 값을 특정값으로 변경
        // arrayList.replaceAll(item -> 4);
        //System.out.println("ArrayList : " + arrayList);

        // 짝수만 필터링
        ArrayList<Integer> evenNumbers = arrayList.stream()
                                             .filter(n -> n % 2 == 0)
                                             .collect(Collectors.toCollection(ArrayList::new));

        System.out.println("ArrayList 짝수만 필터링: " + evenNumbers);
        
        // ArrayList 오름차순 정렬
        Collections.sort(arrayList);

        // ArrayList 내림차순 정렬
        Collections.sort(arrayList, Comparator.reverseOrder());

        // Stream을 사용한 정렬
        ArrayList<Integer> sorted = arrayList.stream()
                                        .sorted()
                                        .collect(Collectors.toCollection(ArrayList::new));

        // Collections.max()로 최대값 찾기
        int max = Collections.max(arrayList);
        System.out.println("ArrayList Max : " + max);

        // Stream을 사용한 총합 구하기
        int sum = arrayList.stream().mapToInt(Integer::intValue).sum();
        System.out.println("ArrayList 총합: " + sum); // 출력: 총합: 150

        //ArrayList[] =======================================================================================================================================================================================================================================

        ArrayList<Integer>[] listArray = new ArrayList[3];

        for(int i = 0; i < 3; i++){
            listArray[i] = new ArrayList<>();
        }

        //ArrayList<ArrayList> =======================================================================================================================================================================================================================================

        ArrayList<ArrayList<Integer>> listList = new ArrayList<>();

        // 내부 ArrayList 추가
        for (int i = 0; i < 3; i++) {
            listList.add(new ArrayList<>());
        }

        Collections.sort(listList, (o1, o2) -> Integer.compare(o1.get(0), o2.get(0)));

        //LinkedList =======================================================================================================================================================================================================================================

        //LinkedList => 삽입삭제많으면 ArrayList 사용, 메소드는 동일
        LinkedList<Integer>linkedList = new LinkedList<>();
        linkedList.add(1);
        linkedList.add(2);
        linkedList.add(3);

        System.out.println("LinkedList : " + linkedList);

        //HashSet ======================================================================================================================================================================================================================================================
        HashSet<Integer> hashSet = new HashSet<>();
        
        hashSet.add(1);
        hashSet.add(1);
        hashSet.add(2);
        hashSet.add(3);

        System.out.println("HashSet : " + hashSet);

        int[][] intArray5 = {{0,100}, {2,10}, {3,1}};
        Arrays.sort(intArray5, (o1, o2) -> Integer.compare(o1[1], o2[1]));
        System.out.println("ComplexArray : " + Arrays.deepToString(intArray5));

        Arrays.stream(intArray5)
              .forEach(item -> System.out.println("Array stream : " + item[0]));

        ArrayList<Node> arrayListNode = new ArrayList<>();

        arrayListNode.add(new Node(1, 100));
        arrayListNode.add(new Node(2, 10));
        arrayListNode.add(new Node(3, 1));

        // 나이로 정렬 (필드를 직접 접근)
        Collections.sort(arrayListNode, (p1, p2) -> p1.first - p2.first);

        // 스트림을 사용하여 first로 정렬 후 출력
        arrayListNode.stream()
                     .sorted((n1, n2) -> n1.second - n2.second)
                     .forEach(item -> System.out.println("first : " + item.first + ", second : " + item.second));

        // ArrayList<Integer> zf = arrayList.stream().filter(z1 ->  z1[0] > z2).toCollection(Collectors.toCollection(ArrayList::new));
        
    }
}
