package abc;

import java.security.Key;
import java.security.SecureRandom;
import java.util.Scanner;
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class zip {

	@SuppressWarnings("resource")
	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		int str = 0;
		System.out.println("1 : Base64");
		System.out.println("2 : YouTube");
		System.out.println("3 : Capital");
		System.out.println("4 : DB");
		System.out.print("-> ");
		Scanner scan = new Scanner(System.in);
		str = scan.nextInt();
		clearScreen();
		switch(str)
        {
            case 1 :
        		String bs;
        		System.out.println("복호화 할 코드를 입력 하세요.");
        		System.out.print("-> ");
        		Scanner bscn = new Scanner(System.in);
        		bs = bscn.nextLine();
        		byte[] v5 = org.apache.commons.codec.binary.Base64.decodeBase64(bs);
        		System.out.println("복호화 전 : " + bs);
        		System.out.println("복호화 후 : " + new String(v5));
                break;
            case 2 :
            	String tube;
            	System.out.println("복호화 할 코드를 입력 하세요.");
        		System.out.print("-> ");
        		Scanner tucn = new Scanner(System.in);  
        		tube = tucn.nextLine();
        		byte[] arg7 = org.apache.commons.codec.binary.Base64.decodeBase64(tube);
        		
        		SecureRandom v0 = new SecureRandom();
        		String arg6 = "Ab5d1Q32";	
        		byte[] v2 = arg6.getBytes("UTF-8");	
        		
        		SecretKeySpec v1 = new SecretKeySpec(v2, "DES");
                
        			Cipher v2_1 = Cipher.getInstance("DES/CBC/PKCS5Padding");	
        	        byte[] v6 = arg6.getBytes();

        	        v2_1.init(2, ((Key)v1), new IvParameterSpec(v6), v0);
        	        
        	        arg7 = v2_1.doFinal(arg7);
        		
        		System.out.println("복호화 전 : "+ new String(tube));
        		System.out.println("복호화 후 : "+ new String(arg7));

                break;
            case 3 :
            	System.out.println("복호화 할 코드를 입력 하세요.");
        		System.out.print("-> ");
            	Scanner sn = new Scanner(System.in);
        		String st = sn.nextLine();
        		//String[] d1 = {"7flMlX9FRY/i5xlUFkS/Bw==", "ZUGLeC0xaDiarEO/1oAqBQ==", "a/JNQAhmlNXR2j0QZrh7LQ==", "oPrrwnMjWc0gDvyQZkp6kA==", "yyjuSyPIVErwP//xUhuIdQ=="};
        		//7flMlX9FRY/i5xlUFkS/Bw==, ZUGLeC0xaDiarEO/1oAqBQ==, a/JNQAhmlNXR2j0QZrh7LQ== , oPrrwnMjWc0gDvyQZkp6kA==, yyjuSyPIVErwP//xUhuIdQ==
        		st = st.replace('"', ' ');
        		st = st.replace(" ", "");
        		String[] d1 = st.split(",");
        		
        		int a = d1.length;
        		try {
        			int v0_1;
        			do {
        				double v01 = Math.random();
        				String[] v21 = d1;
        				double v3 = ((double)v21.length);
        				Double.isNaN(v3);
        				v0_1 = ((int)(v01 * v3));
        			} while (d1[v0_1].isEmpty());
        			// 위에 숫자를 d1[v0_1]이 아무값이 안나올때까지 돌림

        	        SecretKeySpec v01 = new SecretKeySpec("9739DF758A34160C".getBytes(), "AES"); // 지정한 문자열로 AES (암호화 생성)
        	        Cipher v11 = Cipher.getInstance("AES/CBC/PKCS5Padding"); // 암호화 키 주입
        	        v11.init(2, ((Key)v01), new IvParameterSpec("0102030405060708".getBytes())); // 비밀번호
        	        for (int i = 0; i < a; i++) {
        	        	System.out.println("복호화 전 : " +  d1[i]); //doFinal 바이트 한 평문을 암호화
        	        }
        	        for (int i = 0; i < a; i++) {
        	        		byte[] v51 = org.apache.commons.codec.binary.Base64.decodeBase64(d1[i]);
        	        		System.out.println("복호화 후 : " +  new String (v11.doFinal(v51), "UTF-8")); //doFinal 바이트 한 평문을 암호화
        	        }
        		}
        	    catch (Exception e){
                	//e.printStackTrace();
        	    	System.out.println(e);
        	    }
                break;
            case 4 :
        		// TODO Auto-generated method stub
        		String gs;
        		System.out.println("복호화 할 코드를 입력 하세요.");
        		System.out.print("-> ");
        		Scanner gscn = new Scanner(System.in);
        		gs = gscn.nextLine();
        		 byte[] v4 = gs.toString().getBytes(); // 받아온 문자열을 바이트배열로 변환합니다.
                 byte[] v51 = new byte[v4.length]; // 바이트배열의 길이의 개수를 가져옵니다.
                 int v15; // i 대신 v15를 써서 1식 증가할 int(정수)형 변수를 선언합니다.
                 for(v15 = 0; v15 < v4.length; ++v15) { // str 문자열을 가져올떄 까지 v15를 1씩 증가합니다.
                     v51[v15] = ((byte)(v4[v15] + 1)); // v15의 바이트를 1씩 증가해서 v5배열에 저장합니다.
                 }

                 byte[] v61 =org.apache.commons.codec.binary.Base64.decodeBase64(v51);  // 1씩 증가한 v5를 디코딩 해서 v6에 저장해줍니다.
                 byte[] v7 = new byte[v61.length]; // v6 값의 문자열 길이 값을 v7에 저장합니다.
                 for(v15 = 0; v15 < v61.length; ++v15) {   // 똑같이 v15를 이용해 아까 디코딩한 값을 1씩 증가합니다.
                     v7[v15] = ((byte)(v61[v15] + 1)); // 증가 한 값을 v7배열에 저장합니다.
                 }
         		 //System.out.format("Input Data : %s%n", str); // 데이터를 변환합니다.
                 String[] v11 = new String(v7).split(" "); // v7배열에 저장한 값을 utf-8로 변환하고 " "기준으로 저장합니다.
                 dumpArray(v11); // dumpArray변수를 불러옵니다.
                break;
            default :
                
        }
	}

	private static void dumpArray(String[] v1) {
		// TODO Auto-generated method stub
		System.out.format("IP adders : %s%n", v1[0]);  // IP 를 짤라서 가져옵니다.
		System.out.format("Port Number : %s%n", v1[1]); // 포트
		System.out.format("Password : %s%n", v1[2]); // 패스워드
		System.out.format("URL : %s%n", v1[3]); // URL
	}

	private static void clearScreen() {
		// TODO Auto-generated method stub
		 for (int i = 0; i < 80; i++)
		      System.out.println("");
	}

}
