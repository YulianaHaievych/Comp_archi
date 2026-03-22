#!/bin/bash

(sleep 2; exit 7) &

child_pid=$!

echo "Child PID: $child_pid"

wait $child_pid

echo "Child finished with exit code: $?"
