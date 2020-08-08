'''
   This is Script Packet_Dump File

    I hope help you For Enjoy Malware Dynaminc Analysis
    
    License Policy : FSF

'''

import os

def Extracet_Packet():
    
    try:
            conn_cmd = "adb connect 127.0.0.1:62001"
            cmd = "adb -s 127.0.0.1:62001 shell /mnt/shared/Other/./tcpdump -i eth1 -s 65535 -w /mnt/shared/Other/1.pcap"
            Authority_Promotion_cmd = "adb shell chmod 777 /mnt/shared/Other/1.pcap"
            Extract_cmd ="adb -s 127.0.0.1:62001 pull /mnt/shared/Other/1.pcap"
            exc_print = os.popen("adb devices").read().splitlines()    
            if str(exc_print[1]) == "":
                #print ("Not Found Device")
                os.system(conn_cmd)
                os.system(cmd)
            else:
                #print ("Found Device")
                os.system(cmd)
        
    except KeyboardInterrupt as KI:
        #print (" >> "+Authority_Promotion_cmd)
        #print (" >> "+Extract_cmd)
        os.system(Authority_Promotion_cmd)
        os.system(Extract_cmd)
        print("\n >>> Extact Packet_File Complete  \n")


