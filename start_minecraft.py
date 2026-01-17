import os
import subprocess
import urllib
import uuid

import minecraft_launcher_lib as mll
import urllib3
from minecraft_launcher_lib._helper import SUBPROCESS_STARTUP_INFO
from minecraft_launcher_lib.types import CallbackDict


class MCUtils:
    def __init__(self):
        self.command = None

    def download(self):
        # Определение пути по умолчанию для Minecraft директории
        path = mll.utils.get_minecraft_directory()
        print("Installing")
        print("Current path: " + path)
        version = "1.12.2"
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
            "launcherName": "ashaleeeet",  # The name of your launcher
            "launcherVersion": "1.0",  # The version of your launcher
            "jvmArguments": [
                f"-javaagent:authlib-injector.jar=ely.by",  # Полный путь к файлу агента
            ],
            "executablePath": mll.utils.get_java_executable(),  # Исполняемый файл Java
            # "server": "mc.MigosMc.net",  # Сервер, на который подключаемся
            "minecraftDirectory": path,   # Директория Minecraft
            # "quickPlayMultiplayer": "mc.MigosMc.net"
        }



        print("Check minecraft version...")
        mll.install.install_minecraft_version(version=version, minecraft_directory=path)
        print("Download!")
        # mll.forge.install_forge_version()
        # forge = mll.mod_loader.Forge()
        # forge.install("1.12.2", path, CallbackDict(), mll.utils.get_java_executable(), "14.23.5.2768")
        # print(mll.forge.install_forge_version("1.12.2-14.23.5.2768", path))
        #
        install_path = urllib.request.urlretrieve(f"https://ru-minecraft.ru/engine/download.php?id=107720", "install.jar")
        # print(install_path)
        subprocess.run(["java", "-jar", "install.jar"])
        # Получение команды для запуска Minecraft
        self.command = mll.command.get_minecraft_command(version="1.12.2-forge-14.23.5.2860", minecraft_directory=path, options=options)

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
