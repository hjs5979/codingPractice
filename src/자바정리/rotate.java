public class rotate {
    private static int[][] rotate90(int[][] arr){
        int n = arr.length;
        int[][] rotatedArr = new int[n][n];

        for(int i=0; i < n; i++){
            for(int j=0; j < n; j++){
                rotatedArr[j][n-i-1] = arr[i][j];
            }
        }

        return rotatedArr;
    }

    private static int[][] solution(int[][] arr, int n){
        for(int i=0; i < n; i++){
            arr = rotate90(arr);
        }
        return arr;
    }
}
