import java.util.Arrays;

public class combination {
    // 조합 : 순서 상관해서 N개중 R개 선택
    public static void main(String[] args) {
        int n = 4;
        int r = 2;
        int[] arr = {1, 2, 3, 4};
        boolean[] visited = new boolean[n];

        combination(arr, visited, 0, n, 2);
        
    }

    // 백트래킹 사용
    // 사용 예시 : combination(arr, visited, 0, n, r)
    static void combination(int[] arr, boolean[] visited, int start, int n, int r) {
        if (r == 0) {
            System.out.println(Arrays.toString(visited));
            return;
        }

        for (int i = start; i < n; i++) {
            visited[i] = true;
            combination(arr, visited, i + 1, n, r - 1);
            visited[i] = false;
        }
    }

}
