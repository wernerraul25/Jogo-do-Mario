from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None

executables = [Executable("Jogo_do_Mario\main.py",base=base)]

packages = ["pygame"]
options = {
    "build.exe":{
        "packages":packages,
    },

}

setup(
    name="Mario Ninja",
    options = options,
    version = "1.2",
    description = "Jogo do Mario by Werner",
    executables = executables   
)

#o executavel não acontece nada

#python Jogo_do_Mario\setup.py build
#python Jogo_do_Mario\setup.py bdist_msi
