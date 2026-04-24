#!/usr/bin/env python

import os
from dotenv import load_dotenv, dotenv_values
import subprocess

#IP, IP Lat, IP Lon, Provider, Server Name, Server Location, Distance (km), Server Host, Ping, Jitter, Download Speed, Upload Speed
#0      1      2        3          4              5              6               7        8      9           10              11

def main():
	load_dotenv()
	
	logPath = os.getenv("logPath")
	curPath = os.getenv("curPath")
	speedTestPath = os.getenv("speedTestProgPath")
	hostname = os.getenv("hostname")
	
	#result = subprocess.run([speedTestPath, "-o", "csv"], capture_output = True, text = True) 
	testRes = '"136.35.206.146","39.0997","-94.5786","Google Fiber Inc.","Columbus, KS","Optic Communications","215.918","speedtest.optic-communications.com:8080","21","0","889921288.954125","886632212.873472"'
	
	#resArr = result.stdout.split('","')
	resArr = testRes.split('","')
	resArr = [c.replace('"', '') for c in resArr]
	print(resArr)
	for i in range(len(resArr)):
		print(resArr[i])

	print(f'''
Hostname:                      {hostname}
Server Location:               {resArr[5]}
Distance:                      {resArr[6]}
Server Host:                   {resArr[7]}
Ping:                          {resArr[8]}
Download Speed:                {float(resArr[10]):.2f}
Upload Speed:                  {float(resArr[11]):.2f}''')
	
if __name__ == "__main__":
	main()

