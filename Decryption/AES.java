package abc;


import java.security.Key;
import java.util.Scanner;

import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class capital {

	public capital() {
		// TODO Auto-generated constructor stub
	}

	@SuppressWarnings({ "resource", "unused" })
	public static void main(String[] args){
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		String str = scan.nextLine();
		//String[] d1 = {"7flMlX9FRY/i5xlUFkS/Bw==", "ZUGLeC0xaDiarEO/1oAqBQ==", "a/JNQAhmlNXR2j0QZrh7LQ==", "oPrrwnMjWc0gDvyQZkp6kA==", "yyjuSyPIVErwP//xUhuIdQ=="};
		//7flMlX9FRY/i5xlUFkS/Bw==, ZUGLeC0xaDiarEO/1oAqBQ==, a/JNQAhmlNXR2j0QZrh7LQ== , oPrrwnMjWc0gDvyQZkp6kA==, yyjuSyPIVErwP//xUhuIdQ==
		str = str.replace('"', ' ');
		str = str.replace(" ", "");
		String[] d1 = str.split(",");
		
		int a = d1.length;
		try {
			int v0_1;
			do {
				double v0 = Math.random();
				String[] v2 = d1;
				double v3 = ((double)v2.length);
				Double.isNaN(v3);
				v0_1 = ((int)(v0 * v3));
			} while (d1[v0_1].isEmpty());
			// 위에 숫자를 d1[v0_1]이 아무값이 안나올때까지 돌림

	        SecretKeySpec v01 = new SecretKeySpec("9739DF758A34160C".getBytes(), "AES"); // 지정한 문자열로 AES (암호화 생성)
	        Cipher v1 = Cipher.getInstance("AES/CBC/PKCS5Padding"); // 암호화 키 주입
	        v1.init(2, ((Key)v01), new IvParameterSpec("0102030405060708".getBytes())); // 비밀번호
	        for (int i = 0; i < a; i++) {
	        	System.out.println("복호화 전 : " +  d1[i]); //doFinal 바이트 한 평문을 암호화
	        }
	        for (int i = 0; i < a; i++) {
	        		byte[] v5 = org.apache.commons.codec.binary.Base64.decodeBase64(d1[i]);
	        		System.out.println("복호화 후 : " +  new String (v1.doFinal(v5), "UTF-8")); //doFinal 바이트 한 평문을 암호화
	        }
		}
	    catch (Exception e){
        	//e.printStackTrace();
	    	System.out.println(e);
	    }
	}
}
	     