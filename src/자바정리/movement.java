import java.util.Arrays;
import java.util.Scanner;

public class movement {
    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// 상하좌우
		int[] dr = { -1, 1, 0, 0 };
		int[] dc = { 0, 0, -1, 1 };
		// 방향을 저장할 변수(기본 방향은 상).
		int dir = 0;
		// 맵
		boolean[][] map = new boolean[3][3];

		// 명령 입력, 0행 0열부터 시작.
		System.out.print("이동 명령을 입력하세요(Ex : RRDDRDL)(바깥으로 나가면 함수 종료) : ");
		String move = sc.nextLine();
		map[0][0] = true;
		int r = 0, c = 0;
		// 임시로 이동할 좌표를 먼저 설정.
		int nr, nc;

		// 이동
		for (int i = 0; i < move.length(); i++) {
			char a = move.charAt(i);
			System.out.println("움직일 방향 출력 : " + a);
			// 각 문자를 해석해 맞는 방향을 세팅 해준다.
			switch (a) {
			case 'U':
				dir = 0;
				break;
			case 'D':
				dir = 1;
				break;
			case 'L':
				dir = 2;
				break;
			case 'R':
				dir = 3;
				break;
			}
			// 임시로 이동
			nr = r + dr[dir];
			nc = c + dc[dir];
			// 바깥으로 이동하는지 체크하는 if 제어문!!
			if (0 <= nr && nr < 3 && 0 <= nc && nc < 3) {
				r = nr;
				c = nc;
				map[r][c] = true;
			} else {
				System.out.println("바깥으로 이동할 수 없습니다.");
                sc.close();
				return;
			}
			// 현재 맵의 상태 출력
			for (int j = 0; j < 3; j++) {
				System.out.println(Arrays.toString(map[j]));
			}
			System.out.println();
		}
		sc.close();
	}
}
