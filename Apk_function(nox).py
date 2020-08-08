# -*- coding: utf-8 -*-

import hashlib, os
import subprocess
import shutil
import chardet
import math
import glob
import time
import win32com.client as win32

#File output list
def apklist():
    file_list = open("app_list.txt","w")
    C_path = os.getcwd()
    for file_name in os.listdir(C_path):
        #print (os.getcwd()+"\\"+file_list)
        if file_name.endswith(".apk"):
            #d_list.write(file_list)
            #print("APK NAME >> " + file_name)
            #file_size = round(os.path.getsize(file_name)/1024)
            #print("APK File Size >> " + str(file_size) + "KB")
            file_list.write(file_name+"\n")
    file_list.close()

#
# File MD5 Parser
#
    
def find_md5(filename,blocksize = 8192):
    f_md5 = hashlib.md5()
    path = os.getcwd() +"\\"+filename
    try:
        target_file = open(path,"rb")
    except IOError as e:
        print("Error : ",e)
        return

    while True:
        buf = target_file.read(blocksize)
        if not buf:
            break
        f_md5.update(buf)
    #print("APK FILE MD5 Value >> "+str(f_md5.hexdigest()).upper())
    return str(f_md5.hexdigest()).upper()

#
#apk info
#value : package, version, application name , etc\
#

def app_info(filename):   
    if filename.find(" "):  # 파일에 공백이 존재하는경우 처리
        filename = str('"'+filename+'"')
        
    cmd = "aapt d badging "+ filename
    #cmd2 = "aapt d strings " + filename +" | findstr http"
    name_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout
    parser_info = name_popen.read().strip()

    if isinstance(parser_info,bytes):
        data = parser_info.decode('utf-8')
        # Application package value
        package_name = str(data[data.find("package: name"):data.find("versionCode")])
        package_name = package_name.split("=")[1].replace("'", "").strip()
        #print("Package Name >> " + package_name)

        # Application version        
        version = str(data[:data.find("versionName")+18])
        version = version.split(" ")[3]
        version = version.split("=")[1].replace("'","")
        
        # Application name
        if data.find("application: l-") == -1:
            value = str(data[data.find("application: "):data.find("' icon=")])
            value = value.split(": label=")[1].replace("'", "").strip()
           # print("Application name >> "+value)
           #print("\n==============================================\
         
            
        #print(chardet.detect(value))
        return package_name, version, value

        
'''

find_ip, search, find_wedding_ip, find_deilvery_ip <== Smishing Only Function

'''

def find_ip(value,filename):
    if "택배" in value:
        delivery_ip = find_deilvery_ip(filename)
        #print(delivery_ip)
        return delivery_ip
        
    elif "청첩장" in value or "wedding" in value:
        wedding_ip=find_wedding_ip(filename)
        return wedding_ip
    else:
        return "IP 추출 불가"
        
        
def search(dirname):      
    for (path, dir , files) in os.walk(dirname):
        for filename in files:
            ext = os.path.splitext(filename)[0]
            if 'HttpUtils' in ext:
                absoulute_path =os.getcwd() +"\\"+ path +"\\"+ filename
                return absoulute_path

    
    
def find_deilvery_ip(filename):
    cmd = "java -jar apktool_2.2.3.jar d " + filename + " >> null"
    os.system(cmd)
    os.remove("null")
    
    folder_name = str(filename).split(".")[0]  
    get_smail = search(folder_name)    
    smfile = open(get_smail)
    p_file = smfile.read().splitlines()
    smfile.close()    
    
    for parser_line in p_file:
        #print("test")
        if "http:" in parser_line:
            parser_IP = parser_line.split(",")[1].strip('"')
            #print(" >> " + str(parser_IP))
            parser_IP = str(parser_IP).split(":")[1].replace("/","")
            shutil.rmtree(folder_name)
            #print(" >> " + str(parser_IP))
            return parser_IP
        else:
            pass

            
def find_wedding_ip(filename):
    cmd = "aapt d strings " + filename + " | findstr String #20"
    ip_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout
    parser_info = ip_popen.read().strip()
    
    if isinstance(parser_info,bytes):
        data = parser_info.decode('utf-8')
        get_ip = str(data[data.find("String #20:"):])
        get_ip = get_ip.split(":")[2].split("/")[2].replace("'","")
        return get_ip
        


def APK_INFO():
    apklist()
    
    
    parser_list = open("app_list.txt")    
    file_list = parser_list.read().splitlines()
    parser_list.close()
   
    
    for filename in file_list:

        file_size = round(math.ceil(os.path.getsize(filename)/1024.0))
        package_name, version, value = app_info(filename)
        #parser_ip = find_ip(value, filename)
        get_IP = "Unknown"
        
        os.system("adb -s 127.0.0.1:62001 pull /data/data/"+package_name+"/shared_prefs")
        os.system("adb -s 127.0.0.1:62001 shell cat /data/data/"+package_name+"/shared_prefs/"+"pref.xml")
        os.system("adb -s 127.0.0.1:62001 shell cat /data/data/"+package_name+"/shared_prefs/"+"value.xml")
        os.system("adb -s 127.0.0.1:62001 pull /data/data/"+package_name+"/files")
        
        '''
        cmd = input("It is default Smishing?? >> ").lower()        
        global check_value # set local Variable -> global Variable
            
         #print("test >> " + check_value)
        
        if cmd == "t" or cmd == "y":
            parser_value = input("Deviler??(input data 'y') or Wedding(input data 'n')??? >> ").lower()
            if parser_value == "y":
                check_value = "택배"
            else:
                check_value = "wedding"
            get_IP = find_ip(check_value, filename)
        else:
            get_IP = "Unknown"
        
        
        
        리포트를 뽑을때 추출하기위해 객체 형태로 장하는 클래스 내역
        
        
        '''

        print("")
        print("")
        print("\n==================================\n")
        print("APK HASH(MD5) value >> "+find_md5(filename))
        print("APK Filename >> "+filename)
        print("Package Name >> " + package_name)
        print("APK_Version >> " + version)
        version.split()
        version = ' '.join(version.split())
        
        csize = format(file_size, ',')
        print("APK File Size >> " + str(csize) + "KB")
        print("Application name >> " + value)
        #print("Informantion Leak IP Addess >> " + str(get_IP))
        print("\n==================================\n")
        
        
        #한글 보고서에 분석내용 추가
        hwp=win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
        hwp.Open('C:\\Users\\inetcop\\Desktop\\분석\\111.hwp',"HWP","forceopen:true")
        hwp.HAction.GetDefault("AllReplace", hwp.HParameterSet.HFindReplace.HSet);
        option=hwp.HParameterSet.HFindReplace
        
        
        option.FindString = "해시"
        option.ReplaceString = find_md5(filename)
        option.IgnoreMessage = 1
        hwp.HAction.Execute("AllReplace", option.HSet);
        
        option.FindString = "apk34"
        option.ReplaceString = filename
        option.IgnoreMessage = 1
        hwp.HAction.Execute("AllReplace", option.HSet);

        option.FindString = "ver"
        option.ReplaceString = version
        option.IgnoreMessage = 1
        hwp.HAction.Execute("AllReplace", option.HSet);
        
        option.FindString = "pack"
        option.ReplaceString = package_name
        option.IgnoreMessage = 1
        hwp.HAction.Execute("AllReplace", option.HSet);
        
        option.FindString = "MB"
        option.ReplaceString = str(csize) + "KB"
        option.IgnoreMessage = 1
        hwp.HAction.Execute("AllReplace", option.HSet);
        
        option.FindString = '“바”'
        option.ReplaceString = '"'+value+'"'
        option.IgnoreMessage = 1
        hwp.HAction.Execute("AllReplace", option.HSet);
        
        
        #hwp.Clear(3)
        #hwp.Quit()

    print("\n >>> APK INFO Parser Complete!!!!  \n")
    os.system('Pause')
    #time.sleep(5)
    


