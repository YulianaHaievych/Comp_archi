import os

# 1. fork
pid = os.fork()
if pid == 0:
    # ДОЧІРНІЙ ПРОЦЕС
    print("Child process started")
    # exec замінює процес
    os.execlp("bash", "bash", "-lc", "echo Hello from child; exit 7")

else:
    #  БАТЬКІВСЬКИЙ ПРОЦЕС
    print(f"Parent process, child PID: {pid}")

    # чекаємо завершення дитини
    finished_pid, status = os.waitpid(pid, 0)

    # отримуємо exit code
    exit_code = os.WEXITSTATUS(status)
    print(f"Child {finished_pid} finished with exit code: {exit_code}")
