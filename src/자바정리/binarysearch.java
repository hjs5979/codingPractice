public class binarysearch {
    // 이진탐색 로직
	static int[] arr = {1, 3, 5, 7, 8, 10, 20, 35, 99, 100};

	public static void main(String[] args) {
		System.out.println(binarySearch(arr, 10, 0, 10)); // 2
		
	}

    static int binarySearch(int[] array, int target, int start, int end) {
		
        // end가 start보다 큰 동안 반복
        while(start < end) {

			int mid = (start + end)/2;
			
			if(target > array[mid]) {
				start = mid+1;
			}
			else if(target < array[mid]){
				end = mid-1;
			}
			else{
				return mid;
			}
		}
        return -1;
	}
}
