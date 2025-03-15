import java.util.*;

public class DFS {
    class Solution{

        private static ArrayList<Integer>[] adjList;

        private static boolean[] visited;

        private static ArrayList<Integer> answer;

        private static void dfs(int now){
            visited[now] =true;
            answer.add(now);
            for(int next : adjList[now]){
                if(!visited[next]){
                    dfs(next);
                }
            }
        }

        public static void main(String[] args){
            
            int[][] graph = {{'1','2'},{'2','3'},{'3','4'},{'4','5'}};
            int start = '1';
            int n = 5;

            adjList = new ArrayList[n+1];

            for(int i = 0; i < adjList.length; i++){
                adjList[i] = new ArrayList<>();
            }

            for(int[] edge : graph){
                adjList[edge[0]].add(edge[1]);
            }

            visited = new boolean[n+1];
            answer = new ArrayList<>();
            dfs(start);
        
        }

    }
}
