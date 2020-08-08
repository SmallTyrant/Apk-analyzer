package abc;

import java.util.Base64;
import java.util.Base64.Decoder;

public class DB {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str = "LC@yKSLxKS@3Kx/vMx7eLCf2MA73MSDuLSLeY2MyayjtKi@wMh/uKR7sL@<<"; //복호화를 할 코드를 넣어 줍니다. String 사용 이유 = 문자열을 받아오기 위해서 입니다.
		Decoder decode = Base64.getDecoder(); // 자바 내부에 있는 라이브러리인 Base64를 불러오는데 저는 디코더만 사용할거라 디코딩만 합니다.
		 byte[] v4 = str.toString().getBytes(); // 받아온 문자열을 바이트배열로 변환합니다.
         byte[] v5 = new byte[v4.length]; // 바이트배열의 길이의 개수를 가져옵니다.
         int v15; // i 대신 v15를 써서 1식 증가할 int(정수)형 변수를 선언합니다.
         for(v15 = 0; v15 < v4.length; ++v15) { // str 문자열을 가져올떄 까지 v15를 1씩 증가합니다.
             v5[v15] = ((byte)(v4[v15] + 1)); // v15의 바이트를 1씩 증가해서 v5배열에 저장합니다.
         }

         byte[] v6 = decode.decode(v5);  // 1씩 증가한 v5를 디코딩 해서 v6에 저장해줍니다.
         byte[] v7 = new byte[v6.length]; // v6 값의 문자열 길이 값을 v7에 저장합니다.
         for(v15 = 0; v15 < v6.length; ++v15) {   // 똑같이 v15를 이용해 아까 디코딩한 값을 1씩 증가합니다.
             v7[v15] = ((byte)(v6[v15] + 1)); // 증가 한 값을 v7배열에 저장합니다.
         }
 		 System.out.format("Input Data : %s%n", str); // 데이터를 변환합니다.
         String[] v1 = new String(v7).split(" "); // v7배열에 저장한 값을 utf-8로 변환하고 " "기준으로 저장합니다.
         dumpArray(v1); // dumpArray변수를 불러옵니다.
         
	}

	private static void dumpArray(String[] v1) {
		// TODO Auto-generated method stub
		System.out.format("IP adders : %s%n", v1[0]);  // IP 를 짤라서 가져옵니다.
		System.out.format("Port Number : %s%n", v1[1]); // 포트
		System.out.format("Password : %s%n", v1[2]); // 패스워드
		System.out.format("URL : %s%n", v1[3]); // URL
	}

}
