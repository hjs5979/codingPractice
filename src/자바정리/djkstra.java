import java.util.*;

// 인접 리스트 버전
public class djkstra {
    private static class Node{
        int dest, cost;

        public Node(int dest, int cost){
            this.dest = dest;
            this.cost = cost;
        }

    }

    public static void main(String[] args){

        int[][] graph = {{0,1,9},{0,2,3},{1,0,5},{2,1,1}};
        int start = 0;
        int n = 3;

        ArrayList<Node>[] adjList = new ArrayList[n];

        for(int i = 0; i < n; i++){
            adjList[i] = new ArrayList<>();
        }

        for(int[] edge:graph){
            adjList[edge[0]].add(new Node(edge[1], edge[2]));
        }

        int[] dist = new int[n];

        Arrays.fill(dist, Integer.MAX_VALUE);

        dist[start] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> Integer.compare(o1.cost, o2.cost));

        pq.add(new Node(start, 0));

        while(!pq.isEmpty()){
            Node now = pq.poll();

            if(dist[now.dest] < now.cost){
                continue;
            }

            for(Node next : adjList[now.dest]){
                if(dist[next.dest] > now.cost + next.cost){
                    dist[next.dest] = now.cost + next.cost;
                    pq.add(new Node(next.dest, dist[next.dest]));

                }
            }
        }

        System.out.println("dist : " + Arrays.toString(dist));
    }
}
