import java.util.*;

public class BFS {
    private static ArrayList<Integer>[] adjList;

    private static boolean[] visited;

    private static ArrayList<Integer> answer;

    public static void main(String[] args){
        int[][] graph = {{1,2},{1,3},{2,5},{3,6},{3,7},{4,8},{5,8},{6,9},{7,9}};
        int start = 1;
        int n = 9;

        adjList = new ArrayList[n+1];
        for(int i = 0 ; i < adjList.length; i++){
            adjList[i] = new ArrayList<>();
        }

        for(int[] edge : graph){
            adjList[edge[0]].add(edge[1]);
        }

        visited = new boolean[n+1];
        answer = new ArrayList<>();

        bfs(start);

        System.out.println(answer);

    }

    private static void bfs(int start){
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        queue.add(start);
        visited[start] = true;

        while(!queue.isEmpty()){
            int now = queue.poll();

            System.out.println(now);
            
            answer.add(now);

            for(int next : adjList[now]){
                if(!visited[next]){
                    queue.add(next);
                    visited[next] = true;
                }
            }
        }
    }
}
