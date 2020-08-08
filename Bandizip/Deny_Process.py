import subprocess
import os
from datetime import timedelta
from datetime import datetime
from os import chdir

def Deny_Smihing():
    yesterdaylog = 'ex_'+str(datetime.today().date() - timedelta(days=1)).replace('-','')
    chdir('./')    # compress path

#xlsx 
    path = "./"
    file_list = os.listdir(path)
    xlsxzip = [file for file in file_list if file.endswith(".xlsx")]
    xlsxzip = format(xlsxzip).replace("[","")
    xlsxzip = format(xlsxzip).replace("]","")
    xlsxzip = format(xlsxzip).replace(".xlsx","")

    program = 'C:\Program Files\Bandizip\Bandizip.exe'      # 반디집 설치 위치 (Default)
    source = "*.apk"
    source2 = "*.hwp"
    source3 = "*.xml"
    source4 = "*.db"
    dst = format(xlsxzip).replace("'","")+'.zip'
    dst2 = format(xlsxzip).replace("'","")+'_보고서.zip'

    subprocess.run([program,'a','-y','-p:rkadua', dst,source])
    subprocess.run([program,'a','-y', dst2,source2,source3, source4])
    
def removeExtensionFile(filePath, fileExtension):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            if file.name.endswith(fileExtension):
                os.remove(file.path)
        return 'Remove File : ' + fileExtension
    else:
        return 'Directory Not Found'

Deny_Smihing()
removeExtensionFile('./', '.hwp')
removeExtensionFile('./', '.apk')
removeExtensionFile('./', '.xml')
removeExtensionFile('./', '.db')
