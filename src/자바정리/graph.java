import java.util.*;

public class graph {

    private static int[] parent;
    
    private static int find(int x){
        if(parent[x] == x){
            return x;
        }
        parent[x] = find(parent[x]);
        return parent[x];
    }

    private static void union(int x, int y){
        int root1 = find(x);
        int root2 = find(y);

        if (root1 == root2) {
            return;
        }

        parent[root2] = root1;
    }

    public static void main(String[] args){
        
        // int k = 3;
        // int[][] operation = {{0,0,1},{0,1,2},{1,1,2}};

        int k = 7;
        int[][] operation = {
            {1, 6, 5},
            {2, 4, 6},
            {1, 2, 7},
            {3, 5, 15},
            {5, 6, 9},
            {3, 4, 10},
            {1, 3, 11},
            {2, 3, 3},
            {4, 5, 7}};        

        //parent 배열 초기화
        parent = new int[k];
        for(int i = 0; i < k; i++){
            parent[i] = i;
        }

        //최소신장 - 최저 코스트 구하기 (크루스칼 알고리즘)

        //코스트 오름차순으로 정렬한다. 코스트부터 낮은 노드부터 사용
        Arrays.sort(operation, (o1, o2) -> Integer.compare(o1[2], o2[2]));
        System.out.println(Arrays.deepToString(operation));

        int answer = 0;
        int edges = 0;
        
        for(int[] edge : operation){
            
            //최소신장의 경우 노드는 k-1이다.
            if(edges == k-1){
                break;
            }

            //사이클을 잡아내기 위해 체크한다
            if(find(edge[0]) != find(edge[1])){
                union(edge[0], edge[1]);
                System.out.println("edge0 : " + edge[0] + ", edge1 : " + edge[1]);
                answer += edge[2];
                
                edges++;
                
            }
            
        }
        System.out.println(Arrays.toString(parent));
        System.out.println(answer);
    }
}
