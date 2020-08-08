package abc;
 
import java.security.Key;
import java.security.SecureRandom;
import java.util.Scanner;

import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
 
public class youtube {

	@SuppressWarnings("resource")
	public static void main(String[] args) throws Exception {
		
		String str;
		Scanner scan = new Scanner(System.in);  
		str = scan.nextLine();
		byte[] arg5 = org.apache.commons.codec.binary.Base64.decodeBase64(str);
		System.out.println(new String(arg5));
		SecureRandom v0 = new SecureRandom();
		String arg6 = "Ab5d1Q32";	
		byte[] v2 = arg6.getBytes("UTF-8");	
		
		SecretKeySpec v1 = new SecretKeySpec(v2, "DES");
        
			Cipher v2_1 = Cipher.getInstance("DES/CBC/PKCS5Padding");	
	        byte[] v6 = arg6.getBytes();

	        v2_1.init(2, ((Key)v1), new IvParameterSpec(v6), v0);
	        
	        arg5 = v2_1.doFinal(arg5);

		
		System.out.println("복호화 전 : "+ new String(str));
		System.out.println("복호화 후 : "+ new String(arg5));
      
    }
}

