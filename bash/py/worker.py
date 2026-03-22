import signal
import time
import os

stop = False

# Обробка сигналів
def handle_signal(signum, frame):
    global stop
    print(f"\nWorker received signal: {signum}")
    stop = True

signal.signal(signal.SIGINT, handle_signal)
signal.signal(signal.SIGTERM, handle_signal)

print(f"Worker PID: {os.getpid()} starting...")

# Нескінченний цикл
while not stop:
    print("tick")
    time.sleep(1)

print("Worker cleanup before exit...")
time.sleep(1)
print("Worker exiting")
