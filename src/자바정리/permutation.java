import java.util.*;

public class permutation {
    // 순열 : 순서 상관하지 않고 N개중 R개 선택
    public static void main(String[] args) {
        int n = 4;
        int r = 2;
        int[] arr = {1, 2, 3, 4};
        int[] output = new int[r];
        boolean[] visited = new boolean[n];

        perm(arr, output, visited, 0, n, r);
        
    }

    static void perm(int[] arr, int[] output, boolean[] visited, int depth, int n, int r) {
        if (depth == r) {
            System.out.println(Arrays.toString(output));
            return;
        }

        for (int i = 0; i < n; i++) {
            if (visited[i] != true) {
                visited[i] = true;
                output[depth] = arr[i];
                perm(arr, output, visited, depth + 1, n, r);
                visited[i] = false;
            }
        }
    }

}

