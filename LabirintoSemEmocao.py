import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#janela do jogo com titulo e tamanho
def iniciar_jogo():
    janela_jogo = tk.Toplevel()
    janela_jogo.title("Labirinto")
    janela_jogo.geometry("400x400")

    #canvas para o labirinto
    canvas = tk.Canvas(janela_jogo, width=400, height=400, bg="white")
    canvas.pack()

    #caixa que vamos jogar
    caixa = canvas.create_rectangle(20, 20, 40, 40, fill="red")

    #paredes do labirinto (retângulos)
    paredes = [
        canvas.create_rectangle(60, 0, 80, 300, fill="black"),
        canvas.create_rectangle(120, 100, 140, 400, fill="black"),
        canvas.create_rectangle(180, 0, 200, 200, fill="black"),
        canvas.create_rectangle(240, 200, 260, 400, fill="black"),
        canvas.create_rectangle(300, 0, 320, 300, fill="black")
    ]
    #função de colisão define "o que e colisao"
    def colisao_labirinto(objeto, movimento):
        canvas.move(objeto, *movimento)

        objeto_pos = canvas.coords(objeto)

        def checa_colisao(px1, py1, px2, py2):
            return (objeto_pos[0] < px2 and objeto_pos[2] > px1 and objeto_pos[1] < py2 and objeto_pos[3] > py1)
           
    #checar se caixa colide com parede
        colidindo = any(checa_colisao(*canvas.coords(parede)) for parede in paredes)

        canvas.move(objeto, -movimento[0], -movimento[1])
        return colidindo
       
    #define o movimento da caixa
    def mover_caixa(event):
        tecla = event.keysym

        movimento_map ={
            "Up":(0, -20),
            "Down":(0, 20),
            "Left":(-20, 0),
            "Right":(20, 0),
        }
       
    #se a tecla pressionada nao for uma das setas, ignora ela
        if tecla not in movimento_map:
            return
       
        movimento = movimento_map[tecla]
    #se não colidir com nada, ta podendo mover
        if not colisao_labirinto(objeto=caixa, movimento=movimento):
            canvas.move(caixa, *movimento)

#ligar o evento de tecla à função de movimento
    janela_jogo.bind("<Key>", mover_caixa)
	
#função de desligar o joguinho
def fechar_jogo():
    janela.quit()
	
#titulo e tamanho da janela do menu
janela = tk.Tk()
janela.title("Menu jogo")
janela.geometry("400x300")

#titulo, fonte e botoes na tela do menu
titulo = ttk.Label(janela, text="Labirinto", font=("Arial", 20))
titulo.pack(pady=20)
botao_iniciar = ttk.Button(janela, text="Iniciar Jogo", command=iniciar_jogo)
botao_iniciar.pack(pady=10)
botao_fechar = ttk.Button(janela, text="Fechar Jogo", command=fechar_jogo)
botao_fechar.pack(pady=10)

#começa começa começa
janela.mainloop() 
