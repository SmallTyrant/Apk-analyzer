#-*- coding: utf-8 -*-
import time
import os
import shutil





def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                #폴더찾음 - 내부로 들어감
                search(full_filename)
                
            else:
                
                #print(full_filename+"이건 파일 ")
                if answer=="1":
                    findwant(dirname,filename)
                elif answer=="2":
                    findfe(dirname,filename)
                else:
                    print("u must select the 1 or 2")
                #파일찾음 - 조건주고 파일 찾는 부분
                
    except PermissionError:
        pass
    
    
    
    
def findwant(dname,fname):
    #input(dname)  
    f= open("input.txt", "r")
    namelines=f.readlines()
    f.close() 
    for nameline in namelines:
        nameline=nameline.strip("\n")+fe
        #확장자조건추가하자
        #input(nameline)
        if nameline == fname:
            fullnamepath=os.path.join(dname,fname)
            try:
                if cORm=="1":
                    shutil.copy(fullnamepath, parentLocale)
                elif cORm =="2":
                    shutil.move(fullnamepath, parentLocale)
                else:
                    print("u dont insert the 1 or 2")
                    
            except Exception as EE:
                print (EE)
                #input("여기가 에러 넘어가자")
        else:
            print("없어")
        
        
        
def findfe(dname,fname):
    dirNfile=os.path.join(dname,fname)
    
    #input (dname+"@"+fname)
    onlyFilesFE = os.path.splitext(dirNfile)[-1]
    #print(onlyFilesFE)
    if onlyFilesFE == fe:
        #print ("최종 파일 명 : "+fname+" 최종 확장자 명 : "+fe)
        try:
            if cORm=="1":
                shutil.copy(dirNfile, parentLocale)
            elif cORm =="2":
                shutil.move(dirNfile, parentLocale)
            else:
                print("u dont insert the 1 or 2")
        except Exception as e:
            print(e)
        
        
        
        
#main

FOLDER_NAME = time.strftime('%Y%m%dT%H%M%S')
os.mkdir(FOLDER_NAME)
parentLocale=os.path.join(os.getcwd(),FOLDER_NAME)#최상위
print("파일 중복 기준은 파일명, 중복일 경우 패스")
print ("옮겨지는 폴더 경로 : "+parentLocale)
answer=input("input.txt를 이용한 특정 파일명 이동은 1, 특정 확장자 모두 이동은 2 : ")
fe=str(input("찾고자 하는 확장자는? ex).apk, .hwp, .zip 엔터 ! : "))
cORm=input("파일을 복사 하는거면 1, 이동하는거면 2 : ")
print("진행중")


search(os.getcwd())

input("종료하나요?")
