import minecraft_launcher_lib as mll
import subprocess
import os
from urllib import request


def download():
    # Определение пути по умолчанию для Minecraft директории
    path = mll.utils.get_minecraft_directory()
    version = "1.19.1"

    # Скачиваем authlib-injector.jar
    mll.install.install_minecraft_version(version=version, minecraft_directory=path)
    auth = request.urlretrieve("https://authlib-injector.yushi.moe/artifact/55/authlib-injector-1.2.7.jar",
                               "authlib-injector.jar")
    # Версия игры

    # Имя игрока
    nickname = "Guid"

    options = {
        "accessToken": "",
        "clientToken": "",
        "uuid": "",  # Добавлено поле UUID
        "username": nickname,
        "jvmArguments": [
            f"-javaagent:authlib-injector.jar=ely.by"  # Полный путь к файлу агента
        ],
        "executablePath": mll.utils.get_java_executable(),  # Исполняемый файл Java
        "server": "mc.migosmc.net",  # Сервер, на который подключаемся
        "minecraftDirectory": path   # Директория Minecraft
    }



    mll.install.install_minecraft_version(version=version, minecraft_directory=path)
    # Получение команды для запуска Minecraft
    command = mll.command.get_minecraft_command(version=version, minecraft_directory=path, options=options)
    return command


# Функция запуска Minecraft
def start():
    command = download()
    try:
        print("Запускаю сервер...")
        subprocess.run(command)
        os.remove("authlib-injector.jar")
        os.remove("authlib-injector.log")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Запуск игры
if __name__ == "__main__":
    start()