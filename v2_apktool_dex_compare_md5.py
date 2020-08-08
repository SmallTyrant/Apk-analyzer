#-*- coding: utf-8 -*-
import struct
import shutil
import zipfile
import os
import time
import glob
import hashlib


def unzip(source_file, dest_path):
    with zipfile.ZipFile(source_file, 'r') as zf:
        zf.extractall(path=dest_path)
        zf.close()
 
def zip(src_path, dest_file):
    with zipfile.ZipFile(dest_file, 'w') as zf:
        rootpath = src_path
        for (path, dir, files) in os.walk(src_path):
            for file in files:
                fullpath = os.path.join(path, file)
                relpath = os.path.relpath(fullpath, rootpath);
                zf.write(fullpath, relpath, zipfile.ZIP_DEFLATED)
        zf.close()




#dex 유무 확인
def isdex(mm) :
    dex=mm[0:3].decode()
    if dex == 'dex' and len(mm) > 0x70 : # 헤더가 'dex' 문자열로 시작하면서 최소 크기가 0x70 Byte 보다 커야 함
        print("Right Dex File")
        return True
    return False

"""

fp = open('classes.dex', 'rb') 
mm = fp.read() 
fp.close() 
print (isdex(mm))

"""
#헤더 파싱
def header(mm) : 
    magic = mm[0:8] 
    checksum = struct.unpack('<L', mm[8:0xC])[0] 
    sa1 = mm[0xC:0x20] 
    file_size = struct.unpack('<L', mm[0x20:0x24])[0] 
    header_size = struct.unpack('<L', mm[0x24:0x28])[0] 
    endian_tag = struct.unpack('<L', mm[0x28:0x2C])[0] 
    link_size = struct.unpack('<L', mm[0x2C:0x30])[0] 
    link_off = struct.unpack('<L', mm[0x30:0x34])[0] 
    map_off = struct.unpack('<L', mm[0x34:0x38])[0] 
    string_ids_size = struct.unpack('<L', mm[0x38:0x3C])[0] 
    string_ids_off = struct.unpack('<L', mm[0x3C:0x40])[0] 
    type_ids_size = struct.unpack('<L', mm[0x40:0x44])[0]
    type_ids_off = struct.unpack('<L', mm[0x44:0x48])[0] 
    proto_ids_size = struct.unpack('<L', mm[0x48:0x4C])[0] 
    proto_ids_off = struct.unpack('<L', mm[0x4C:0x50])[0] 
    field_ids_size = struct.unpack('<L', mm[0x50:0x54])[0] 
    field_ids_off = struct.unpack('<L', mm[0x54:0x58])[0] 
    method_ids_size = struct.unpack('<L', mm[0x58:0x5C])[0] 
    method_ids_off = struct.unpack('<L', mm[0x5C:0x60])[0] 
    class_defs_size = struct.unpack('<L', mm[0x60:0x64])[0] 
    class_defs_off = struct.unpack('<L', mm[0x64:0x68])[0] 
    data_size = struct.unpack('<L', mm[0x68:0x6C])[0] 
    data_off = struct.unpack('<L', mm[0x6C:0x70])[0] 
    hdr = {}
    
    if len(mm) != file_size : # 헤더에 기록된 파일 크기 정보와 실제 파일의 크기가 다르면 분석을 종료한다. 
        return hdr
    hdr['magic' ] = magic 
    hdr['checksum' ] = checksum 
    hdr['sa1' ] = sa1 
    hdr['file_size' ] = file_size 
    hdr['header_size' ] = header_size 
    hdr['endian_tag' ] = endian_tag 
    hdr['link_size' ] = link_size 
    hdr['link_off' ] = link_off 
    hdr['map_off' ] = map_off 
    hdr['string_ids_size'] = string_ids_size 
    hdr['string_ids_off' ] = string_ids_off
    hdr['type_ids_size' ] = type_ids_size 
    hdr['type_ids_off' ] = type_ids_off 
    hdr['proto_ids_size' ] = proto_ids_size 
    hdr['proto_ids_off' ] = proto_ids_off 
    hdr['field_ids_size' ] = field_ids_size 
    hdr['field_ids_off' ] = field_ids_off 
    hdr['method_ids_size'] = method_ids_size
    hdr['method_ids_off' ] = method_ids_off 
    hdr['class_defs_size'] = class_defs_size 
    hdr['class_defs_off' ] = class_defs_off
    hdr['data_size' ] = data_size
    hdr['data_off' ] = data_off 
    return hdr
"""
hdr = header(mm) 
print hdr
"""
"""
print hdr['string_ids_size'] # 전체 문자열 개수 
print hex(hdr['string_ids_off']) # 전체 문자열의 시작 위치
"""
"""
전체 문자열의 시작 위치에서 4Byte를 읽어서 출력한다. (첫번째 문자열의 시작 위치) 
string_off = struct.unpack('<L', mm[off:off+4])[0]
print hex(string_off)
"""
"""
off = off + (4*5) # 4Byte씩 각 문자열의 위치 정보가 있으므로 6번째 문자열의 위치정보를 얻는다.
print hex(off) # 전체 문자열의 시작 위치에서 4Byte를 읽어서 출력한다. (첫번째 문자열의 시작 위치) 
string_off = struct.unpack('<L', mm[off:off+4])[0] 
print hex(string_off)
"""
"""
string_off = 0x14fc0 # 5번째 문자열의 위치 
string_len = ord(mm[string_off]) # 문자열의 길이 
string_val = mm[string_off+1:string_off+1+string_len] # 문자열 추출 
print string_len 
print string_val
"""

def type_id_list(mm, hdr) :
    type_list = [] # 전체 Type 정보를 담을 리스트
    type_ids_size = hdr['type_ids_size' ]
    type_ids_off = hdr['type_ids_off' ]
    for i in range(type_ids_size) :
        idx = struct.unpack('<L',mm[type_ids_off+(i*4):type_ids_off+(i*4)+4])[0]
        type_list.append(idx)
    return type_list


"""
type_ids = type_id_list(mm, hdr)
for i in range(len(type_ids)) :
    string_idx = type_ids[i]
    print '[%4d] %s' % (i, string_ids[string_idx])
    """





#전체 문자열 추출
def string_id_list(mm, hdr) : 
    string_id = [] # 전체 문자열을 담을 리스트
    string_ids_size = hdr['string_ids_size'] 
    string_ids_off = hdr['string_ids_off' ] 
    for i in range(string_ids_size) : 
        off = struct.unpack('<L', mm[string_ids_off+(i*4):string_ids_off+(i*4)+4])[0] 
        c_size = ord(mm[off]) 
        c_char = mm[off+1:off+1+c_size] 
        string_id.append(c_char) 
    return string_id


"""
string_ids = string_id_list(mm, hdr) # 전체 문자열 출력하기 
for i in range(len(string_ids)) : 
    print '[%4d] %s' % (i, string_ids[i])
"""

#전체 필드_패키지이름+클래스이름
def field_id_list(mm, hdr) :
    field_list = []
    field_ids_size = hdr['field_ids_size' ]
    field_ids_off = hdr['field_ids_off' ]
    for i in range(field_ids_size) :
        class_idx = struct.unpack('<H',mm[field_ids_off+(i*8) :field_ids_off+(i*8)+2])[0]
        type_idx = struct.unpack('<H',mm[field_ids_off+(i*8)+2:field_ids_off+(i*8)+4])[0]
        name_idx = struct.unpack('<L',mm[field_ids_off+(i*8)+4:field_ids_off+(i*8)+8])[0]
        field_list.append([class_idx, type_idx, name_idx])
    return field_list

"""
field_ids = field_id_list(mm, hdr)
# 전체 문자열 출력하기
for i in range(len(field_ids)) :
    (class_idx, type_idx, name_idx) = field_ids[i]
    class_str = string_ids[type_ids[class_idx]]
    type_str = string_ids[type_ids[type_idx]]
    name_str = string_ids[name_idx]
    mag = '%s %s.%s' % (type_str, class_str, name_str)
    print '[%4d] %s' % (i, mag)
"""

#전체 메소드 출력하기
def method_id_list(mm, hdr) :
    method_list = []
    method_ids_size = hdr['method_ids_size' ]
    method_ids_off = hdr['method_ids_off' ]
    for i in range(method_ids_size) :
        class_idx = struct.unpack('<H',mm[method_ids_off+(i*8) :method_ids_off+(i*8)+2])[0]
        proto_idx = struct.unpack('<H',mm[method_ids_off+(i*8)+2:method_ids_off+(i*8)+4])[0]
        name_idx = struct.unpack('<L', mm[method_ids_off+(i*8)+4:method_ids_off+(i*8)+8])[0]
        method_list.append([class_idx, proto_idx, name_idx])
    return method_list

"""
전체 메소드 출력하기
method_ids = method_id_list(mm, hdr)
for i in range(len(method_ids)) :
    (class_idx, proto_idx, name_idx) = method_ids[i]
    class_str = string_ids[type_ids[class_idx]]
    name_str = string_ids[name_idx]

    print ('[%04d] %s.%s()' % (i, class_str, name_str))
"""

"""
def desxml(an):
    print (an)
    an=str(an)
    an=an.strip()
    print an
    os.system('java -jar AXMLPrinter2.jar '+an+'/AndroidManifest.xml > '+an+'/4adxml.txt')
"""


def pic_pack(an2):
    
    f = open('_'+an2+'/AndroidManifest.xml')
    f2 = open(an2+'/1result.txt','a')
    ff=f.readlines()
    for fline in ff:
        if 'package="' in fline:
            f2.write('\n\n\n')
            f2.write(fline)
            """print >>fline, allresut
            print >>"\n\n@@@@@@@@@@@@@@\n\n",allresut"""
            allresut.write("\n")
            allresut.write(fline)
            allresut.write("\n")
            f2.close()
            print fline
            nn
    f.close()
    
'''
def apktool(an3):
    os.system('java -jar apktool_2.1.1.jar d '+an3+'.apk -o _'+an3)
def pic_name(an4):
    f = open('_'+an4+'/res/values/strings.xml')
    f2 = open(an4+'/1result.txt','a')
    ff=f.readlines()
    for fline in ff:
        if '<string name="app_name">' in fline:
            f2.write('\n\n\n')
            f2.write(fline)
            """print >>fline, allresut
            print >>"\n\n@@@@@@@@@@@@@@\n\n",allresut"""
            allresut.write(fline)
            allresut.write("\n\n@@@@@@@@@@@@@@@@@@@@@@@\n\n")
            f2.close()
            print fline
            
    f.close()    
''' 

#filepath = apk이름
#


#apk->md5로파일이름변환
def changename(filepath2,funcmd5_):
    funcmd5apk=funcmd5_+'.apk'
    try:
        os.rename(filepath2, funcmd5_+'.apk')
        print ('변환 %s -> %s\n' % (filepath2, funcmd5apk))
    except:
        os.remove(filepath2)
        print("중복 - 삭제 %s\n" % filepath2)
        
    


#파일의 md5얻어오기
def funcMd5(filepath, blocksize=8192):
    md5 = hashlib.md5()
    try:
        f = open(filepath, "rb")
    except IOError as e:
        print("file open error", e)
        return
    while True:
        buf = f.read(blocksize)
        if not buf:
            break
        md5.update(buf)
    md5s.append(md5.hexdigest().upper())



#main
###################################################################################
allresut=open('allresut.txt', 'w')

md5s=[]
i=0
#glob.glob('')
#원하는 문자열이 포함된 파일들을 뽑아냄 _ 리스트형식
for name in glob.glob('*.apk'):
    print (name)
    #allresut.write(name)
    #allresut.write("\n")
    funcMd5(name)
    print (md5s[i])
    #allresut.write(md5s[i])
    #allresut.write("\n")
    changename(name, md5s[i])
    i+=1



for md5 in md5s:
    apkname=md5
    print md5
    allresut.write(md5)
    allresut.write("\n")    

    #Main#Main#Main#Main#Main#Main#Main#Main#Main#Main#Main#Main#Main#Main#Main#Main#Main#Main#Main#Main#Main#Main#Main#Main#Main#Main#Main#Main#Main#
    #apkname=raw_input("apk name?")
    fullapkname=apkname+".apk"
    #apktool(apkname)
    unzip(fullapkname, apkname)
    
    #shutil.move(fullapkname, apkname)
    #shutil.copy2("./v2_read_dex_compare.py", apkname)
    #os.system("python27 ./"+apkname+"/v2_read_dex_compare.py")
    
    
    
    
    
    a=[]
    b=[]
    
    
    method=open(apkname+"/2method.txt", "w")
    string=open(apkname+"/3string.txt", "w")
    fp = open(apkname+'/classes.dex', 'rb')
    mm = fp.read() 
    fp.close() 
    isdex(mm)
    hdr = header(mm)
    
    string_ids = string_id_list(mm, hdr)
    method_ids = method_id_list(mm, hdr)
    type_ids = type_id_list(mm, hdr)
    
    
    
    ####################
    print "All Method : %d"%(hdr['method_ids_size'])
    print >>method, "All Method : %d"%(hdr['method_ids_size'])
    for i in range(len(method_ids)) :
        (class_idx, proto_idx, name_idx) = method_ids[i]
        class_str = string_ids[type_ids[class_idx]]
        name_str = string_ids[name_idx]
    
        #print ('[%04d] %s.%s()' % (i, class_str, name_str))
        #print >>method, '[%04d] %s.%s()' % (i, class_str, name_str)
        print ('.%s' % (name_str))
        a.append(name_str)
        print >>method, ('%s' % (name_str))
        
    method.close()
    ####################
    print "All String : %d"%(hdr['string_ids_size'])
    print >>string,"All String : %d"%(hdr['string_ids_size'])
    for i in range(len(string_ids)) : 
        #print '[%04d] .%s' % (i, string_ids[i])
        #print >>string, '[%04d] .%s' % (i, string_ids[i])
        print '%s' % (string_ids[i].strip())
        b.append(string_ids[i].strip())
        print >>string, '%s' % (string_ids[i].strip())
    
    
    c=[]
    c=a+b
    string.close()
    
    #print c
    
    
    
    
    
    word=['deviceinfo',['getdeviceid', 'imei', 'imsi', 'getsubscriverid', 'getsimserialnumber']
          ,'tongsinsa',['getnetworkoperatorname','getnetworkoperator','getnetworktype']
          ,'kernel',['release', 'build']
          ,'num',['getline1number']
          ,'contact',['contact','mimetype','display_name','_id','_name']
          ,'sms',['sms','smssend','getmessagebody','body','getcontentresolver','abortbroadcast','getoriginatingaddress','getdisplayoriginatingaddress','getdisplaymessagebody','pdus','createfrompdu','sms_send','sms_delivered']
          ,'calling',['new_outgoing_call','incommingnumber','recording','outgoingcall']
          ,'gps',['gps','latitude','longtitude','getlatitude','getlongitude']
          ,'sotr_np',['getexternalstoragedirectory','mounted','getabsolutepath','npki']
          ,'install_send',['install','remove','sendmultiparttextmessage','sendtextmessage']
          ,'hide_cont',['getcomponentname','startswith']
          ,'admin_dontdell',["device_admin", 'devoce_policy', 'explanation','isadminactive']
          ,'etc',['gmail.com','smtp','webview','loadurl','geturl','http://','host','hostname','loadlibrary','getnetworktype','getactivenetworkinfo','audio','setringermode']
          ,'spy',['getcookiestore']]
    
    
    
    """
    
    deviceinfo=['getdeviceid', 'imei', 'imsi', 'getsubscriverid', 'getsimserialnumber']
    tongsinsa=['getnetworkoperatorname','getnetworkoperator','getnetworktype']
    kenel=['release', 'build']
    num=['getline1number']
    contact=['contact','mimetype','display_name','_id','_name']
    sms=['sms','smssend','getmessagebody','body','getcontentresolver','abortbroadcast','getoriginatingaddress','getdisplayoriginatingaddress','getdisplaymessagebody','pdus','createfrompdu','sms_send','sms_delivered']
    calling=['new_outgoing_call','incommingnumber','recording','outgoingcall']
    gps=['gps','latitude','longtitude','getlatitude','getlongitude']
    sotr_np=['getexternalstoragedirectory','mounted','getabsolutepath','npki']
    install_send=['install','remove','sendmultiparttextmessage','sendtextmessage']
    hide_cont=['getcomponentname','startswith']
    admin_dontdell=["device_admin", 'devoce_policy', 'explanation','isadminactive']
    etc=['gmail.com','smtp','webview','loadurl','geturl','http://','host','hostname','loadlibrary','getnetworktype','getactivenetworkinfo','audio','setringermode']
    
    
    """
    result=open(apkname+'/1result.txt','w')
    
    for ic in range(len(c)):
        c[ic]=c[ic].lower()
        
    
    final=[]
    
    for i in range(len(word)):
        if i%2==0:
            print 'i is zzak %d' %i
            continue
        else:
            """print i-1
            print 'i is hol'
            print word[i]
            print word[i][0]
            print len(word[i])"""
            for ii in range(len(word[i])):
                """print ii
                print word[i][ii]"""
                for iii in range(len(c)):
                    """print c[iii]
                    print word[i][ii]"""
                    if c[iii] == word[i][ii]:
                        if word[i-1] not in final:
                            final.append("\n"+word[i-1]+"----------")
                            final.append(c[iii]+"/")
                            break
                        else:
                            final.append(c[iii]+"/")
                            break
                        #print i
                        #print word[i]
                        #print word[i-1]
                        #print c[iii]
                        #input("what?")
                        
                        #print c[iii]
                        #print >>result, c[iii]
                        
                        
                        
    #final=list(set(final))
    print final
    for finall in final:
        result.write(finall)
        allresut.write(finall)
        #allresut.write("\n")       

    result.close()
    #desxml(apkname)
    
    """try:"""
    pic_pack(apkname)
    #pic_name(apkname)
    shutil.move("_"+apkname, apkname)
    shutil.move(fullapkname, apkname)        
    """except:
du
     input("?")
        print 'fail'"""
        
    
    
    
        
        
        
allresut.close()
    
                        
                    
                
        
        
    
    
    
    
    
