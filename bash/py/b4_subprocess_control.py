import subprocess
import os
import signal
import time

# 1. Запускаємо процес sleep 100
proc = subprocess.Popen(["sleep", "100"])

print(f"Process started with PID: {proc.pid}")

# 2. Надсилаємо SIGSTOP
time.sleep(1)
os.kill(proc.pid, signal.SIGSTOP)
print("Process stopped (SIGSTOP)")

# Перевіряємо статус (Unix)
# через ps
time.sleep(1)
subprocess.run(["ps", "-o", "pid,stat,comm", "-p", str(proc.pid)])

# 3. Надсилаємо SIGCONT
time.sleep(1)
os.kill(proc.pid, signal.SIGCONT)
print("Process continued (SIGCONT)")

time.sleep(1)
subprocess.run(["ps", "-o", "pid,stat,comm", "-p", str(proc.pid)])

# 4. Завершуємо процес (SIGTERM)
time.sleep(1)
proc.terminate()  # надсилає SIGTERM
proc.wait()
print("Process terminated (SIGTERM)")
print(f"Return code: {proc.returncode}")
