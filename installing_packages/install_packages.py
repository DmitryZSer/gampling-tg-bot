import subprocess
import sys

def install_packages():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Все библиотеки успешно установлены.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при установке пакетов: {e}")

if __name__ == "__main__":
    install_packages()
