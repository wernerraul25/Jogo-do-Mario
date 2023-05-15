import cx_Freeze
executables =[
    cx_Freeze.Executable(script="Jogo_do_Mario\main.py")
]

cx_Freeze.setup(
    name = "Mario Ninja",
    options = {
        "build_exe":{
            "packages":["pygame"],
            "include_files":["Jogo_do_Mario\mariofundo.jpg",
                             "Jogo_do_Mario\cano.png",
                             "Jogo_do_Mario\hbomba.png",
                             "Jogo_do_Mario\mario.png",
                             "Jogo_do_Mario\musicmario.wav",
                             "Jogo_do_Mario\partiuabomba.mp3",
                             "Jogo_do_Mario\perdedor.mp3",
                             "Jogo_do_Mario\wee.wav"]
        }
    }, executables = executables
)

#python Jogo_do_Mario\gera_setup.py build
#python Jogo_do_Mario\gera_setup.py bdist_msi
#msi microsoft installer
