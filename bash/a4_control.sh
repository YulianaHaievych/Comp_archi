#!/bin/bash

sleep 100 &
PID=$!

echo "Process started with PID: $PID"
sleep 1

kill -STOP $PID
echo "Process stopped (SIGSTOP)"
ps | grep $PID

sleep 1

kill -CONT $PID
echo "Process continued (SIGCONT)"
ps | grep $PID

sleep 1

kill -TERM $PID
echo "Process terminated (SIGTERM)"
sleep 1
ps | grep $PID

