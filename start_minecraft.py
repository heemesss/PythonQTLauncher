import os
import subprocess
import urllib
import uuid

import minecraft_launcher_lib as mll


def download():
    # Определение пути по умолчанию для Minecraft директории
    path = mll.utils.get_minecraft_directory()
    version = "1.21.4"

    # Скачиваем authlib-injector.jar
    mll.install.install_minecraft_version(version=version, minecraft_directory=path)
    auth = urllib.request.urlretrieve("https://authlib-injector.yushi.moe/artifact/55/authlib-injector-1.2.7.jar",
                               "authlib-injector.jar")
    # Версия игры

    # with open(path + "")
    options = {
        "uuid": uuid.uuid4().hex,  # Добавлено поле UUID
        "username": "Guid",
        "token": "",
        "jvmArguments": [
            f"-javaagent:authlib-injector.jar=ely.by",  # Полный путь к файлу агента
            "-Xmx2G"
        ],
        "executablePath": mll.utils.get_java_executable(),  # Исполняемый файл Java
        # "server": "mc.MigosMc.net",  # Сервер, на который подключаемся
        "minecraftDirectory": path,   # Директория Minecraft
        "quickPlayMultiplayer": "mc.MigosMc.net"
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
        # os.remove("authlib-injector.jar")
        # os.remove("authlib-injector.log")
        print(f"Произошла ошибка: {e}")

# Запуск игры
if __name__ == "__main__":
    start()
