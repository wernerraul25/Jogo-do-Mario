import cx_Freeze
executables =[
    cx_Freeze.Executable(script="main.py", icon="icone.ico")
]

cx_Freeze.setup(
    name = "Mario Ninja",
    options = {
        "build_exe":{
            "packages":["pygame"],
            "include_files":["bomba.png",
                             "cano.png",
                             "fundo.jpg",
                             "icone.png",
                             "mario.png",
                             "musicmario.wav",
                             "partiuabomba.mp3",
                             "perdedor.mp3",
                             "wee.wav"]
        }
    }, executables = executables
)


#funcionando
#python gera_setup.py build
#python gera_setup.py bdist_msi
#msi microsoft installer