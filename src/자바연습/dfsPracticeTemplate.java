import java.util.ArrayList;

public class dfsPracticeTemplate {

        private static ArrayList<Integer> answer;

        public static void main(String[] args){

            // 파라미터1 : [부모노드, 자식노드]
            int[][] tree = {{1,2},{1,3},{2,4},{2,5},{3,5},{3,6}};

            // 파라미터2 : 시작 노드
            int startNode = 1;
            
            // 파라미터3 : 노드 개수
            int n = 6;

            answerCheck();
        
        }

        private static void dfs(){
            
        }

// ==================================================================================================================================================
        // 재귀함수를 통해 구현 

        // 인접리스트배열 선언, 방문배열 선언, 정답리스트 선언

        // dfs 함수 정의
        // 파라미터 : 노드
        // 1. 해당 노드 방문처리
        // 2. 해당 노드 정답에 넣기
        // 3. 인접리스트배열에서 해당 노드의 자식 노드들 하나씩 꺼내서 방문하지 않았다면  dfs함수에 자식노드 넣기

        // 메인 함수
        // 1. 인접리스트배열 초기화
        // 2. 인접리스트 초기화
        // 3. 인접리스트배열 부모노드 인덱스에 자식노드 넣기
        // 4. 방문배열 초기화
        // 5. 정답리스트 초기화
        // 6. dfs함수에 시작노드 넣기

        private static void answerCheck(){

            System.out.println("     1 : " + answer);
            System.out.println("Answer : [1, 2, 4, 5, 3, 6]");

        }
}
