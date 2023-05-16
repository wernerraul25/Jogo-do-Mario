import cx_Freeze
executables =[
    cx_Freeze.Executable(script="main.py")
]

cx_Freeze.setup(
    name = "Mario Ninja",
    options = {
        "build_exe":{
            "packages":["pygame"],
            "include_files":["mariofundo.jpg",
                             "cano.png",
                             "hbomba.png",
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
