import ftplib

def connect_to_ftp():
    host = input("Введите FTP хост: ")
    port = int(input("Введите порт (обычно 21): "))
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    
    while True:
        try:
            ftp = ftplib.FTP()
            ftp.connect(host, port)
            ftp.login(username, password)
            print("Подключение к FTP успешно установлено.")
            ftp.quit()  # Отключаемся от FTP
            print("Отключение от FTP выполнено.")
        except ftplib.all_errors as e:
            print(f"Ошибка подключения: {e}")
            choice = input("Хотите попробовать снова? (да/нет): ")
            if choice.lower() != 'да':
                break

if __name__ == "__main__":
    connect_to_ftp()
