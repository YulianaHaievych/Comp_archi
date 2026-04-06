import threading

valid_passwords = []
lock = threading.Lock()

def is_valid(password):
    if len(password) < 8:
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    return True

def check_passwords(password_list):
    for password in password_list:
        if is_valid(password):
            with lock:
                valid_passwords.append(password)

passwords = [
    "abc123", "Password1", "HELLO123", "short",
    "ValidPass9", "testTest", "Qwerty123"
]
chunks = [passwords[:3], passwords[3:5], passwords[5:]]
threads = []
for chunk in chunks:
    t = threading.Thread(target=check_passwords, args=(chunk,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("Правильні паролі:", valid_passwords)