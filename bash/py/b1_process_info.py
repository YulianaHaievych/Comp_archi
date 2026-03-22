import os
import subprocess
pid = os.getpid()
ppid = os.getppid()
print(f" My PID: {pid}")
print(f" My PPID: {ppid}")
print("\nProcess info from ps:")
subprocess.run(["ps"])