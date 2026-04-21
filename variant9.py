import subprocess

def main():
    input_text = "привіт, я текст із батьківського процесу!"
    print(f"Відправляємо: {input_text}")

    process = subprocess.Popen(
        ["python3", "-c", "import sys; text = sys.stdin.read(); print(text.upper())"],
        stdin=subprocess.PIPE,  
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE, 
        text=True               
    )
    stdout_data, stderr_data = process.communicate(input=input_text)

    if stderr_data:
        print(f"Сталася помилка: {stderr_data}")
    else:
        print(f"Отримано від дочірнього процесу: {stdout_data.strip()}")

if __name__ == "__main__":
    main()