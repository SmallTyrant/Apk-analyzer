#-*- coding: utf-8 -*-
import socket
import os
import json
import urllib.request

r = open('whois2.txt', mode='r', encoding='utf-8')
lines = r.readlines()
whois_key = '2019111811330574298381'


for line in lines:
    line = line.replace("\n","")
    addr1 = socket.gethostbyname(line)
    
    query = "http://whois.kisa.or.kr/openapi/whois.jsp?query=" + addr1 + "&key="+ whois_key + "&answer=json";
    request = urllib.request.urlopen(query).read().decode("utf-8")
    dict = json.loads(str(request))
    hop = ( str(line) + '\t' + str(addr1) + '\t' + str(dict['whois']['countryCode']))
    f = open("./whois.txt", 'a+')
    f.write(str(hop)+'\n')
    f.close()
    print("Success")
    
r.close()

#다른 방식
#query2 = "http://whois.kisa.or.kr/openapi/ipascc.jsp?query" + addr1 + "&key="+ whois_key + "&answer=json";
#print(query2)