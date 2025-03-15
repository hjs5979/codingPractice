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

        //스택
        Stack<Integer> stack = new Stack<>();
        
        //뒤로 삽입
        stack.push(1);
        stack.push(2);
        stack.push(3);

        System.out.println("Stack : " + stack);

        //맨 뒤의 값 반환
        int a = stack.peek();

        //맨 뒤의 값 반환하고 삭제
        int b = stack.pop();

        System.out.println("Stack peek : " + a);
        System.out.println("Stack pop : " + b);

        

        //큐
        Queue<Integer> queue = new ArrayDeque<>();

        //뒤로 삽입
        queue.add(1);
        queue.add(2);
        queue.add(3);

        System.out.println("Queue : " + queue);

        //맨 앞의 값 반환
        int c = queue.peek();

        //맨 앞의 값 반환하고 삭제
        int d = queue.poll();

        System.out.println("Queue peek : " + c);
        System.out.println("Queue poll : " + d);

        //데크
        ArrayDeque<Integer> deque = new ArrayDeque<>();
        
        deque.add(1);

        System.out.println("Deque : " + deque);

        //뒤로 삽입
        deque.addLast(2);

        //앞으로 삽입
        deque.addFirst(3);
        
        //collection 타입(List : stack, ArrayList, queue, deque / Set : HashSet 등) 그대로 뒤로 삽입
        deque.addAll(stack);

        //맨 앞의 값 반환
        int e = deque.peek();
        int f = deque.peekFirst();
        int first = deque.getFirst();

        //맨 앞의 값 반환하고 삭제
        int g = deque.poll();
        int h = deque.pollFirst();

        //맨 뒤의 값 반환
        int i = deque.peekLast();
        int last = deque.getLast();

        //맨 뒤의 값 반환하고 삭제
        int j = deque.pollLast();

        System.out.println("Deque peek : " + e);
        System.out.println("Deque peekFisrt : " + f);
        System.out.println("Deque getFirst : " + first);

        System.out.println("Deque poll : " + g);
        System.out.println("Deque pollFirst : " + h);

        System.out.println("Deque peekLast : " + i);
        System.out.println("Deque getLast : " + last);

        System.out.println("Deque pollLast : " + j);

        //ArrayList
        ArrayList<Integer> arrayList = new ArrayList<>();
        arrayList.add(1);
        arrayList.add(2);
        arrayList.add(3);

        System.out.println("ArrayList : " + arrayList);

        //인덱스 값 추출
        int k = arrayList.get(0);

        //인덱스로 값 변경
        arrayList.set(0, 0);
        System.out.println("ArrayList index 1: " + arrayList.get(0));

        //ArrayList 두개 합칠때 사용
        arrayList.addAll(arrayList);
        System.out.println("ArrayList 두개 합칠때 사용 : " + arrayList);

        //전부 삭제
        //arrayList.clear();

        //원소 포함 여부 확인
        boolean l = arrayList.contains(1);
        System.out.println("ArrayList 원소 포함 여부 : " + l);

        //ArrayList끼리 비교해서 포함 여부 확인
        boolean m = arrayList.containsAll(arrayList);
        System.out.println("ArrayList끼리 비교해서 포함 여부 확인 : " + m);

        //값으로 인덱스 추출
        int o = arrayList.indexOf(0);
        System.out.println("ArrayList 값으로 인덱스 추출" + o);

        //비어있는지 확인
        boolean p = arrayList.isEmpty();
        System.out.println("ArrayList 비어있는지 확인 : " + p);

        //forEach 사용법
        arrayList.forEach(q -> System.out.println("ArrayList forEach 사용법 : " + q));

        // 값이 나오는 마지막 인덱스
        int r = arrayList.lastIndexOf(3);
        System.out.println("ArrayList 값이 나오는 마지막 인덱스 : " + r);

        //인덱스의 값을 제거
        arrayList.remove(0);

        //모든 값을 특정값으로 변경
        //arrayList.replaceAll(item -> 4);
        //System.out.println("ArrayList : " + arrayList);

        // 짝수만 필터링
        List<Integer> evenNumbers = arrayList.stream()
                                             .filter(n -> n % 2 == 0)
                                             .collect(Collectors.toList());

        System.out.println("ArrayList 짝수만 필터링: " + evenNumbers);
        
        // ArrayList 오름차순 정렬
        Collections.sort(arrayList);

        // ArrayList 내림차순 정렬
        Collections.sort(arrayList, Comparator.reverseOrder());

        // Stream을 사용한 정렬
        List<Integer> sorted = arrayList.stream()
                                        .sorted()
                                        .collect(Collectors.toList());

        // Collections.max()로 최대값 찾기
        int max = Collections.max(arrayList);
        System.out.println("ArrayList Max : " + max);

        // Stream을 사용한 총합 구하기
        int sum = arrayList.stream().mapToInt(Integer::intValue).sum();
        System.out.println("ArrayList 총합: " + sum); // 출력: 총합: 150

        //LinkedList => 삽입삭제많으면 ArrayList 사용, 메소드는 동일
        LinkedList<Integer>linkedList = new LinkedList<>();
        linkedList.add(1);
        linkedList.add(2);
        linkedList.add(3);

        System.out.println("LinkedList : " + linkedList);

        //HashSet
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

        ArrayList<Integer> zf = arrayList.stream().filter(z1 ->  z1[0] > z2).toCollection(Collectors.toCollection(ArrayList::new));
        
    }
}
