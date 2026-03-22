import signal
import time
import os

stop = False

# 1. handler (обробник сигналів)
def handle_signal(signum, frame):
    global stop
    print(f"\nReceived signal: {signum}")
    stop = True


# 2. реєструємо сигнали
signal.signal(signal.SIGINT, handle_signal)
signal.signal(signal.SIGTERM, handle_signal)

print(f"Process PID: {os.getpid()}")

# 3. головний цикл
while not stop:
    print("tick")
    time.sleep(1)

# 4. cleanup
print("Cleaning up before exit...")
time.sleep(1)

print("Done. Exiting.")
