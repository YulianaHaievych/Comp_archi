import subprocess
import time
import signal

MAX_RESTARTS = 3
restart_count = 0
stop = False

def handle_signal(signum, frame):
    global stop
    print("\nSupervisor received Ctrl+C, stopping...")
    stop = True

signal.signal(signal.SIGINT, handle_signal)

while restart_count < MAX_RESTARTS and not stop:
    print(f"\nSupervisor starting worker (attempt {restart_count+1})...")
    
    proc = subprocess.Popen(["python3", "worker.py"])
    
    try:
        proc.wait()
    except KeyboardInterrupt:
        print("Supervisor interrupted, terminating worker...")
        proc.terminate()
        proc.wait()
        break

    print(f"Worker exited with return code: {proc.returncode}")
    
    restart_count += 1
    if restart_count < MAX_RESTARTS:
        print("Supervisor restarting worker...\n")
        time.sleep(1)

print("Supervisor exiting.")
