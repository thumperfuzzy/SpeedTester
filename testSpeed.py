#!/usr/bin/env python

import os
from dotenv import load_dotenv, dotenv_values
import subprocess
from datetime import datetime
import time
import traceback

#IP, IP Lat, IP Lon, Provider, Server Name, Server Location, Distance (km), Server Host, Ping, Jitter, Download Speed, Upload Speed
#0      1      2        3          4              5              6               7        8      9           10              11

def getTestRes():
	load_dotenv()


	timestamp = datetime.now()
	logPath = os.getenv("logPath")
	curPath = os.getenv("curPath")
	hostname = os.getenv("hostname")
	speedTestPath = os.getenv("speedTestProgPath")
	
	result = subprocess.run([speedTestPath, "-o", "csv"], capture_output = True, text = True) 
	#testRes = '"136.35.206.146","39.0997","-94.5786","Google Fiber Inc.","Columbus, KS","Optic Communications","215.918","speedtest.optic-communications.com:8080","21","0","889921288.954125","886632212.873472"'
	return result

def main():
	attempts = 1
	load_dotenv()
	
	timestamp = datetime.now()
	logPath = os.getenv("logPath")
	curPath = os.getenv("curPath")
	hostname = os.getenv("hostname")
	speedTestPath = os.getenv("speedTestProgPath")
	
	result = getTestRes()
	resArr = result.stdout.split('","')
	#resArr = testRes.split('","')
	resArr = [c.replace('"', '') for c in resArr]

	try:
		while(result.returncode == 1 and attempts < 10):
			attempts += 1
			print(f"retrying. Attempt {attempts}")
			time.sleep(60)
			result = getTestRes()
	except:
		print(f"{result} failed while retrying")
	
	try:
		with open(logPath, "a") as f:
			if attempts < 10:
				f.write(f"| {hostname:^15} | {timestamp} | {resArr[4]:^20} | {float(resArr[6]):^8.4f} | {float(resArr[8]):^7.2f} | {(float(resArr[10])/1000/1000):^15.2f} | {(float(resArr[11])/1000/1000):^15.2f} |\n")
			else:
				f.write(f"{timestamp} {result.sderr}")
	except Exception:
		print(f"{result} failed to write file")
		print(traceback.format_exc())
		






if __name__ == "__main__":
	main()

