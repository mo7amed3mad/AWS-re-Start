import subprocess
import os

ips=open("ping.txt","r")
lines = ips.readlines()

for ip in lines:
    ip = ip.rstrip()
    out = subprocess.Popen(["ping","-c","1",ip],stdout=subprocess.PIPE).communicate()[0]
    
    if "icmp_seq" in str(out):
        print("ip : "+ip+" --> machine is up")
    else:
        print("ip : "+ip+" --> machine is down")
print("end of pinging ips in file")
ips.close()