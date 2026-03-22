#!/bin/bash

cleanup() {
 echo "cleanup..."
 exit 0
}

trap cleanup SIGINT SIGTERM

i=1

while true
do
 echo "tick=$i"
 ((i++))
 sleep 1
done
