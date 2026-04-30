#!/usr/bin/env bash
touch log.txt
echo "|    Hostname     |          Timestamp         |    Server Location   | Distance |  Ping   |    Download     |     Upload      |" > log.txt

echo "curPath = ${PWD}" > .env
echo "logPath = `realpath log.txt`" >> .env
echo "speedTestProgPath = `realpath ./SpeedTest/SpeedTest`" >> .env
echo "hostname = `hostname`" >> .env
