import java.util.*;

// 인접행렬 버전
public class djkstraTemplate2 {

    // 동서남북 이동 
    static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};

    // 행렬 벗어났는지 확인
    private static boolean isValidMove(int l, int nx, int ny){
        return 0 <= nx && nx < l && 0 <= ny && ny < l;
    }

    // x, y, cost 를 가진 Class
    private static class Node{
        int x, y, cost;

        public Node(int x, int y, int cost){
            this.x = x;
            this.y = y;
            this.cost = cost;
        }
    }


    public static void main(String[] args){

        int n = 3;

        int[][] map = {{0,1,9},{0,2,3},{1,0,5}};

        // 우선순위 큐 ( cost로 정렬 )
        PriorityQueue<Node> que = new PriorityQueue<>((o1, o2) -> Integer.compare(o1.cost, o2.cost));
        
        // 첫번째 노드 추가
        que.add(new Node(0, 0, 0));
        
        // cost 계산 결과 map
        int[][] move = new int[n][n];

        // move MAX_VALUE로 초기화
		for(int i=0; i<n; i++) {
			Arrays.fill(move[i], Integer.MAX_VALUE);
		}

        // move 시작 노드 설정
        move[0][0] = map[0][0];

        while(!que.isEmpty()){

            // que에서 하나 뺌
            Node now = que.poll();

            int nowX = now.x;
            int nowY = now.y;
            int nowCost = now.cost;

            // 최종 노드면 끝 
            if(nowX == n-1 && nowY == n-1) {
				System.out.println(nowCost);
			}

            for(int i = 0; i < 4; i++){
                
                int nextX = nowX + dx[i]; 
                int nextY = nowY + dy[i];
                
                //행렬 벗어나면 for문으로 돌아감
                if(!isValidMove(n, nextX, nextY)){
                    continue;
                }

                // 계산 cost가 작으면 변경
                if(move[nextY][nextX] > nowCost + map[nextY][nextX]) {
					move[nextY][nextX] = nowCost + map[nextY][nextX];
					que.add(new Node(nextX, nextY, nowCost + map[nextY][nextX]));
				}

            }

        }

        answerCheck(move, n);
    }

// ============================================================================================================================================================================================================================================

    // 좌표이동 배열 선언 

    // 행렬 벗어났는지 확인하는 함수
    // 파라미터 : 행렬 크기, x, y

    // 노드 클래스 생성

    // 메인 함수
    // 1. 배열 선언
    // 2. 우선순위큐 선언 - 비용순으로
    // 3. 큐에 0,0,0 삽입
    // 4. 최소 비용 배열 선언
    // 5. 최소 비용 배열 큰 수로 채우기
    // 6. 최소 비용 배열에 시작 좌표 초기화
    // 7. 큐가 빌 때까지, while
    //   7-1. 큐에서 하나 빼기
    //   7-2. 현재 x,y,cost 초기화
    //   7-3. 최종 노드면 끝
    //   7-4. 동서남북 for문 시작
    //       7-4-1. 다음 좌표 계산
    //       7-4-2. 다음 좌표가 행렬 벗어났는지 확인하는 함수에 넣기
    //       7-4-3. 다음 좌표의 최소 비용 > 현재 좌표 비용 + 다음좌표 비용 이면 다음 좌표 최소 비용 초기화
    //       7-4-4. 큐에 넣기



    private static void answerCheck(int[][] answerArray, int n){

        System.out.println("     1 : " + answerArray[n-1][n-1]);
        System.out.println("Answer : 6");

    }

}
