import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 인접행렬 버전
public class djkstra2 {
    
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

    // 다익스트라 함수
    static int Dijkstra(){

        int n = 3;
        int[][] map = {{0,1,9},{0,2,3},{1,0,5}};

        // 우선순위 큐 ( cost로 정렬 )
        PriorityQueue<Node> que = new PriorityQueue<>((o1, o2) -> Integer.compare(o1.cost, o2.cost));
        
        // 첫번째 노드 추가
        que.add(new Node(0, 0, 0));
        
        // cost 계산 결과 map
        int[][] move = new int[n][n];

        // move 시작 노드 설정
        move[0][0] = map[0][0];

        // move MAX_VALUE로 초기화
		for(int i=0; i<n; i++) {
			Arrays.fill(move[i], Integer.MAX_VALUE);
		}

        while(!que.isEmpty()){

            // que에서 하나 뺌
            Node now = que.poll();

            int nowX = now.x;
            int nowY = now.y;
            int nowCost = now.cost;

            // 최종 노드면 끝 
            if(nowX == n-1 && nowY == n-1) {
				return nowCost;
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
        return -1;

    }

}
