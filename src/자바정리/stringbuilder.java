import java.util.Arrays;
import java.util.stream.IntStream;

public class stringbuilder {
    public static void main(String[] args){
        
        //문자열 초기화
        StringBuilder stringBuilder = new StringBuilder("TEST");

        //문자열 추가
        stringBuilder.append("ER");

        //문자열 중간 삽입
        stringBuilder.insert(2, "L");

        //특정 구간 문자열 삭제
        stringBuilder.delete(3,4);
        
        //특정 인덱스 문자 삭제
        stringBuilder.deleteCharAt(3);

        //특정 구간 문자열 대체
        stringBuilder.replace(3, 6, "AB");

        //특정 인덱스 문자열 대체
        stringBuilder.setCharAt(4, 'o');

        //문자열 슬라이싱
        stringBuilder.substring(3, 5);

        //특정 위치 문자열
        stringBuilder.charAt(2);

        //스트링빌더를 문자 배열로 생성
        char[] charArray = stringBuilder.toString().toCharArray();

        //스트링빌더를 문자열 배열로 생성
        String[] stringArray = stringBuilder.toString().split("");

        //StringBuffer와 StringBuilder의 차이는 thread-safe여부에 있다. 코테에서는 StringBuilder를 사용하자
    }
}
