package abc;

import java.util.Scanner;

public class base64 {

	@SuppressWarnings("resource")
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str;
		Scanner scan = new Scanner(System.in);  
		str = scan.nextLine();
		byte[] v5 = org.apache.commons.codec.binary.Base64.decodeBase64(str);
		System.out.println("복호화 전 : " + str);
		System.out.println("복호화 후 : " + new String(v5));
	}

}
