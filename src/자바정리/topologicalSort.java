import java.util.*;

public class topologicalSort {

    static private int v = 9;
    static private int e = 8;
    static private int[] indegree;
    static private ArrayList<ArrayList<Integer>> graph;
    static private ArrayList<Integer> result;
    public static void main(String[] args){
        
        int[][] input = {{1,2},{1,4},{4,2},{2,5},{2,6},{4,8},{8,6},{7,3},{3,6}};

        // 진입차수
        indegree = new int [e+1];

        graph = new ArrayList<>();

        for(int i = 0; i < input.length; i++){
            graph.add(new ArrayList<>());
        }

        for(int i = 0; i < input.length; i++){
            graph.get(input[i][0]).add(input[i][1]);
            indegree[input[i][1]] += 1;
        }

        topologySort();

        System.out.println(result);

    }

    public static void topologySort(){
        result = new ArrayList<>();

        Queue<Integer> queue = new ArrayDeque<>();

        for(int i = 1; i < e+1; i++){
            if(indegree[i] == 0){
                queue.add(i);
            }
        }

        while(!queue.isEmpty()){
            int now = queue.poll();

            result.add(now);

            for(int i = 0; i < graph.get(now).size() ; i++){
                indegree[graph.get(now).get(i)] -= 1;
                if(indegree[graph.get(now).get(i)] == 0){
                    queue.add(graph.get(now).get(i));
                }
                    
            }

        }

    }
}
