import pygame

pygame.init()
pygame.mixer.init()

#variaveis do jogo
altura = 720
largura = 1280
#tamanho = (1280,720)
black = (0,0,0)
white = (255,255,255)
fps = 144
dificuldade = 7

#cria a pontuação e fonte
pontuacao = 0
fonte = pygame.font.Font(None,36) #cria uma fonte com tamanho 36
fonte_meme = pygame.font.Font(None,50) #cria fonte com tamanho 50

mario = pygame.image.load("mario.png")
fundo = pygame.image.load("fundo.jpg")
cano = pygame.image.load("cano.png")
bomba = pygame.image.load("bomba.png")
icone = pygame.image.load("icone.png")

musica_mario = pygame.mixer.Sound("musicmario.wav")  #carrega a musica
musica_mario.play(-1) #deixa a musica jogo todo
musica_mario.set_volume(0.1) #regula o volume da música

#carrega wee
som_pulo = pygame.mixer.Sound("wee.wav")
som_pulo.set_volume(0.1)

#carrega som da bomba
som_bomba = pygame.mixer.Sound("partiuabomba.mp3")
som_bomba.set_volume(0.1)

#carrega som final
som_final = pygame.mixer.Sound("perdedor.mp3")
som_final.set_volume(0.1)

#texto de meme impossivel na pontuação 50
texto_meme = fonte_meme.render("AAAAAAAAAAA TENTA AGORA",True,white)

clock = pygame.time.Clock()
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Mario ninja")
pygame.display.set_icon(icone)

#posições mario, cano e bomba
posicao_canox = 1400
posicao_canoy = 495
largura_cano = 150
altura_cano = 170
posicao_mariox = 300
posicao_marioy = 475
posicao_bombax = 2100
posicao_bombay = 480
largura_bomba = 295
altura_bomba = 214

#variaveis do pulo
gravidade = 0.8
y_pulo = 0
pulando = False

modo_jogo = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not pulando:
            y_pulo = -30
            pulando = True
            som_pulo.play()
            pontuacao += 1 #cada pulo aumenta um ponto
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP and not pulando:
            y_pulo = -30
            pulando = True
            som_pulo.play()
            pontuacao += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w and not pulando:
            y_pulo = -30
            pulando = True
            som_pulo.play()
            pontuacao += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            posicao_canox = 1400
            posicao_canoy = 495
            largura_cano = 150
            altura_cano = 170
            posicao_mariox = 300
            posicao_marioy = 475
            posicao_bombax = 2100
            posicao_bombay = 480
            largura_bomba = 295
            altura_bomba = 214
            pontuacao = 0
            modo_jogo = 1

    if modo_jogo == 1:

        # Atualiza a posição vertical do personagem
        posicao_marioy += y_pulo
        y_pulo += gravidade
        
        #verifica se o personagem ta no chão
        if posicao_marioy >= altura - 245:
            posicao_marioy = altura - 245
            pulando = False

        #o que aparece na tela
        tela.blit(fundo,(0,0))
        tela.blit(cano,(posicao_canox,posicao_canoy))
        posicao_canox = posicao_canox - dificuldade #cano se move pra esquerda
        tela.blit(mario,(posicao_mariox,posicao_marioy))
        tela.blit(bomba,(posicao_bombax,posicao_bombay))
        posicao_bombax = posicao_bombax - dificuldade #a bomba se move pra esquerda

        #mostra pontuação
        texto_pontuacao = fonte.render("Pontuação: " + str(pontuacao), True, white)
        tela.blit(texto_pontuacao,(10,10))

        #verifica colisão do cano
        if posicao_mariox < posicao_canox + largura_cano and \
        posicao_mariox + 50 > posicao_canox and \
        posicao_marioy < posicao_canoy + altura_cano and \
        posicao_marioy + 50 > posicao_canoy:
            modo_jogo = 2 

        #verifica colisão da bomba
        if posicao_mariox < posicao_bombax + largura_bomba and \
        posicao_mariox + 50 > posicao_bombax and \
        posicao_marioy < posicao_bombay + altura_bomba and \
        posicao_marioy + 50 > posicao_bombay:
            modo_jogo = 2

        #cano volta pro lado esquerdo da tela
        if posicao_canox <= -1280:
            posicao_canox = 1280
        #bomba volta pro lado esquerdo da tela
        if posicao_bombax <= - 1280:
            posicao_bombax = 1280
        
        #som da bomba
        if posicao_bombax == 1280:
            som_bomba.play()

        #aumenta dificuldade
        if pontuacao == 5:
            dificuldade = 8
        elif pontuacao == 10:
            dificuldade = 9
        elif pontuacao == 15:
            dificuldade = 10
        elif pontuacao == 20:
            dificuldade = 11
        elif pontuacao >= 50:
            dificuldade = dificuldade + 1
            tela.blit(texto_meme,(415,200))

    #caso perca vai aparecer a segunda tela
    elif modo_jogo == 2:
        texto_fim = fonte.render("O jogo acabou!",True,white)
        texto_fim2 = fonte.render("Sua pontuação foi: " + str(pontuacao), True, white)
        tela.blit(texto_fim,(530,320))
        tela.blit(texto_fim2,(525,360))
        
        #para os sons
        som_pulo.stop()
        som_bomba.stop()
        musica_mario.stop()
        
        #som de final
        som_final.play()

    pygame.display.update()
    clock.tick(fps)

pygame.quit() 