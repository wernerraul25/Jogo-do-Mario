import cx_Freeze
executables =[
    cx_Freeze.Executable(script="Jogo_do_Mario\main.py")
]

cx_Freeze.setup(
    name = "Mario Ninja",
    options = {
        "build_exe":{
            "packages":["pygame"],
            "include_files":["Jogo-do-Mario\mariofundo.jpg",
                             "Jogo-do-Mario\cano.png",
                             "Jogo-do-Mario\hbomba.png",
                             "Jogo-do-Mario\mario.png",
                             "Jogo-do-Mario\musicmario.wav",
                             "Jogo-do-Mario\partiuabomba.mp3",
                             "Jogo-do-Mario\perdedor.mp3",
                             "Jogo-do-Mario\wee.wav"]
        }
    }, executables = executables
)

#python Jogo-do-Mario\gera_setup.py build
#python Jogo-do-Mario\gera_setup.py bdist_msi
#msi microsoft installer
