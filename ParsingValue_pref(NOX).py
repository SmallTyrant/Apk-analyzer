# -*- coding: cp949 -*-
import os
import subprocess
import codecs
import zipfile

def getApklist() :
    f_apk = open("apklist.txt", "w")
    folder = os.getcwd()
    for filename in os.listdir(folder):
        if filename.endswith('apk'):
            f_apk.write(filename[:-4]+"\n")
    f_apk.close() 

def parseData():
    f_apk = open("apklist.txt")
    f_report = codecs.open("report.txt",'w','utf-8')
    
    lines = f_apk.read().splitlines()
    f_apk.close()    

    print (lines)
    for md5 in lines :      
        f_popen = os.system("java -jar apktool.jar d "+md5+".apk")

    print (lines)
    for md5 in lines :

 
        menifest = codecs.open('.\\'+md5+'\\AndroidManifest.xml','r','utf-8')
        yml = codecs.open('.\\'+md5+'\\apktool.yml','r','utf-8')
        strings = codecs.open('.\\'+md5+'\\res\\values\\strings.xml','r','utf-8')
        sha_path = '.\\'+md5+'\\original\\META-INF'
        file_list = os.listdir(sha_path)
        cert_rsa = ''
        for rsa in file_list:
            if rsa.endswith('RSA'):
                cert_rsa = sha_path + "\\" +rsa
        sha = subprocess.Popen("keytool -printcert -file "+cert_rsa, stdout=subprocess.PIPE).stdout
       
        data1 = menifest.read().strip()
        data2 = yml.read().strip()
        data3 = strings.read().strip()
        data4 = sha.read().strip()
 
        menifest.close()
        yml.close()
        strings.close()
        sha.close()
        
        data1=str(data1)    
        data2=str(data2)    
        data3=str(data3)
        data4=str(data4)    

        print ("\n\n")
        print ("MD5 \t\t: " + md5)


        data1 = data1[data1.find("package=")+9:]
        pkg = data1[:data1.find('"')]
        print ("Package \t: " + pkg)
  
        data2 = data2[data2.find("versionName:")+12:]
        ver = data2.replace("'","").replace(" ","")
        print ("version \t: " + ver)

  
        if data3.find("app_name") != -1 :
            data3 = data3[data3.find("app_name")+10:]
            nm = data3[:data3.find("string>")-2]
        elif data3.find("application_name") != -1 :
            data3 = data3[data3.find("application_name")+18:]
            nm = data3[:data3.find("string>")-2]
        elif data3.find("product_name") != -1 :
            data3 = data3[data3.find("product_name")+14:]
            nm = data3[:data3.find("string>")-2]
        elif data1.find("activity android:label=") != -1 :
            data3 = data1[data1.find("activity android:label=")+24:]
            nm = data3[:data3.find(" ")-1]
        else :
            nm = "+ Parse Error +"
        print ("app_name \t: " + nm)

     
        data4 = data4[data4.find("SHA1:"):data4.find("SHA256:")-5]
        data4 = data4.replace(":","")
        sha1 = data4[5:]
        print("SHA1 \t\t: " + sha1)

        try:
            os.system("adb kill-server")
            os.system("adb connect 127.0.0.1:62001")
            os.system("adb shell ls -R /data/data/"+pkg+" > "+md5+"_pkg.txt")
            os.system("adb shell ls -R /data/data/"+pkg+"/shared_prefs/ > tmp_"+md5+".txt")          # CJ write txt  

            t_cj = 1 
            t_wedding = 2 
            ftmp = open("tmp_"+md5+".txt", 'r')
            lines = ftmp.readlines()
            for line in lines:
                line = line.replace('\n',"")
                if line.endswith('pref.xml'):
                    type = t_cj
                    xmlname = line
                    break
                elif line.endswith('preferences.xml'):
                    type = t_cj
                    xmlname = line
                    break
                else:
                    xmlname = 'no have xml file'


            xmlprint = "cat_"+md5+".txt"
            f = open(xmlprint,'w')
            print ("\nroot@x86:/data/data/"+pkg+"/shared_prefs # cat "+xmlname,file=f)
            f.close()
    
            
            #print ("\n")
            print ("XML File name\t: "+xmlname)
        
            os.system("adb shell cat /data/data/"+pkg+"/shared_prefs/"+xmlname+" >> cat_"+md5+".txt")  

            fip = open("cat_"+md5+".txt","r")
            dataip = fip.read().strip()
            fip.close()
            dataip = dataip[dataip.find("http://")+7:]
            dataip = dataip[:dataip.find("/")]
            dataip = dataip.replace("/","")
            print("IP Addr\t\t: " + dataip)
    
            
            os.system("type cat_"+md5+".txt")  
        
        
                
            print (pkg+"\t"+nm+"\t"+ver+"\t"+md5+"\t"+sha1, file=f_report)
        except file:
            print("error")
    f_report.close()
    
def main():
    getApklist()
    parseData()



