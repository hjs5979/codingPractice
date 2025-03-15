import java.io.*;
import java.util.*;

class test{
    
    // private static class Node{
    //     int dest, cost;

    //     public Node(int dest, int cost){
    //         this.dest = dest;
    //         this.cost = cost;
    //     }
    // }
    
    private static boolean isValidMove(int l, int nx, int ny){
        return 0 <= nx && nx < l && 0 <= ny && ny < l;
    }
    
    public static void main(String[] args) throws IOException{
        int n = -1;

        int[][] move = {{0,1}, {1,0}};

        while(n != 0){
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            
            n = Integer.parseInt(br.readLine());
            
            // ArrayList<Node>[] adjList = new ArrayList[n];

            // for(int i = 0; i < n; i++){
            //     adjList[i] = new ArrayList<>();
            // }

            int[][] map = new int[n][n];
            boolean[][] visited = new boolean[n][n];

            int[][] cost = new int[n][n];

            Arrays.fill(cost, Integer.MAX_VALUE);

            for(int i = 0; i < n; i++){
                String c = br.readLine();
                String[] strList = c.split(" ");
                
                for(int j = 0; j < strList.length; j++){
                    int jcost =  Integer.parseInt(strList[j]);
                    map[i][j] = jcost;
                }
            }

            cost[0][0] = map[0][0];

            Queue<int[]> que = new ArrayDeque(); 
            que.add(new int[]{0,0});

            while(que.isEmpty()){

                int[] nxny = que.poll();

                int nowx = nxny[0];
                int nowy = nxny[0];

                for(int i = 0; i < move.length; i++){
                    
                    int nextx = nowx + move[i][0]; 
                    int nexty = nowy + move[i][1]; 

                    if(!isValidMove(n, nextx, nexty)){
                        continue;
                    }

                    que.add(new int[]{nextx, nexty});

                    int calc = map[nowx][nowy] + map[nextx][nexty];

                    if(map[nextx][nexty] >= calc){
                        cost[nextx][nexty] = calc;
                    }
    
                }

            }



            System.out.println(cost[n-1][n-1]);
        }
        


    }
}