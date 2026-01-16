import os
import subprocess
import urllib
import uuid

import minecraft_launcher_lib as mll

class MCUtils:
    def __init__(self):
        self.command = None

    def download(self):
        # Определение пути по умолчанию для Minecraft директории
        path = mll.utils.get_minecraft_directory()
        print("Current path: " + path)
        version = "1.21.4"
        print("Current version: " + version)

        # Скачиваем authlib-injector.jar
        print("Download authlib-injector.jar...")
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
            ],
            "executablePath": mll.utils.get_java_executable(),  # Исполняемый файл Java
            # "server": "mc.MigosMc.net",  # Сервер, на который подключаемся
            "minecraftDirectory": path,   # Директория Minecraft
            "quickPlayMultiplayer": "mc.MigosMc.net"
        }



        print("Check minecraft version...")
        mll.install.install_minecraft_version(version=version, minecraft_directory=path)
        print("Download!")
        # Получение команды для запуска Minecraft
        self.command = mll.command.get_minecraft_command(version=version, minecraft_directory=path, options=options)

    # Функция запуска Minecraft
    def start(self):
        try:
            print("Запускаю сервер...")
            subprocess.run(self.command)
        except Exception as e:
            print(f"Произошла ошибка: {e}")

# Запуск игры
if __name__ == "__main__":
    mc = MCUtils()
    mc.start()
