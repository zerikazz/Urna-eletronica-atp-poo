from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
import pygame
from eleicao_ar import *

window = tk.Tk()
window.title("Urna eletrônica")
window.geometry("1100x1100")  
window.configure(bg='black')

input_number = ""
pygame.init()
pygame.mixer.init(frequency= 1600)

# Funcao teste antes de importar eleicao_ar

# def get_eleitor_info(eleitor_number): FUNÇÃO PARA PEGAR O TITULO ELEITORAL DO ELEITOR ANTES DE COMEÇAR A VOTAÇÃO


def get_candidato_info(candidato_number):
    candidatos = {
        '93': {
            'nome': 'Andressa Urach',
            'partido': 'Jacaré',
            'vice': 'Marido da Lana Del Rey',
            'image': 'andressa.png',  
            'vice_image': 'marido_lana.png' 
        }
    }
    return candidatos.get(candidato_number, None)

#def tocar_som():
    #pygame.mixer.music.load('bip.mp3')  
    #pygame.mixer.music.play() 

def tocar_som():
    try:
        pygame.mixer.music.load('teclas/bip.mp3')  
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:  
            pygame.time.Clock().tick(10)
    except pygame.error as e:
        print(f"Erro ao carregar o som: {e}")

def press_key(key):
    global input_number  
    tocar_som()

    if key == 'Confirmar':
            ve_imagem()
            pygame.mixer.music.load('teclas/confirma-urna.mp3')
            pygame.mixer.music.play()
    
    if key == 'Branco':
            ve_imagem()
            pygame.mixer.music.load('teclas/confirma-urna.mp3')
            pygame.mixer.music.play()

    elif key.isdigit():
        input_number += key 
        print(f"Tecla pressionada: {key}, Número atual: {input_number}")
        if len(input_number) == 2: 
            ver_candidato_info(input_number)  

    else:
        print(f"Tecla pressionada: {key}")

# imagem Justiça Eleitoral
def ve_imagem():
    global img_label
    try:
        img = Image.open("justica_eleitoral.png")
        img = img.resize((int(img.width * 0.65), int(img.height * 1.3)), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        
        img_label.config(image=img)
        img_label.image = img
    except Exception as e:
        print("Erro ao carregar a imagem:", e)
        return

def ver_candidato_info(candidato_number):
    candidato_info = get_candidato_info(candidato_number)
    
    candidato_label.config(text=f"Nome: {candidato_info['nome']}\n"
                                f"Partido: {candidato_info['partido']}\n"
                                f"Vice-presidente: {candidato_info['vice']}")
    
    # imagens
    try:
        candidato_image = Image.open(candidato_info['image'])
        candidato_image = candidato_image.resize((150, 150), Image.LANCZOS)
        candidato_image = ImageTk.PhotoImage(candidato_image)
        candidato_image_label.config(image=candidato_image)
        candidato_image_label.image = candidato_image
        candidato_image_label.place(relx=0.5, rely=0.4, anchor='n')  
    except Exception as e:
        print("Erro ao carregar a imagem do candidato:", e)
    
    try:
        vice_image = Image.open(candidato_info['vice_image'])
        vice_image = vice_image.resize((125, 125), Image.LANCZOS)
        vice_image = ImageTk.PhotoImage(vice_image)
        vice_image_label.config(image=vice_image)
        vice_image_label.image = vice_image
        vice_image_label.place(relx=0.5, rely=0.6, anchor='n')  
    except Exception as e:
        print("Erro ao carregar a imagem do vice:", e)

# Frames para layout
left_frame = tk.Frame(window, bg='white')
left_frame.pack(side="left", fill="y", padx=20, pady=20) 
right_frame = tk.Frame(window, bg='black')
right_frame.pack(side="right", fill="y", padx=20, pady=(200, 0))

img_label = tk.Label(left_frame, bg='black')
img_label.pack(side="top", padx=10, pady=20)  

candidato_label = tk.Label(left_frame, bg='white', fg='black', font=('Arial', 16), justify="left")
candidato_label.pack(side="top", padx=10, pady=20)

candidato_image_label = tk.Label(left_frame)
candidato_image_label.place(relx=0.5, rely=0.4, anchor='n') 
vice_image_label = tk.Label(left_frame)
vice_image_label.place(relx=0.5, rely=0.6, anchor='n')  

def teclas(image_path, size=(20, 20)):
    nums = Image.open(image_path)
    nums = nums.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(nums)

nums = {
    '1': 'teclas/n1.png',
    '2': 'teclas/n2.png',
    '3': 'teclas/n3.png',
    '4': 'teclas/n4.png',
    '5': 'teclas/n5.png',
    '6': 'teclas/n6.png',
    '7': 'teclas/n7.png',
    '8': 'teclas/n8.png',
    '9': 'teclas/n9.png',
    '0': 'teclas/n0.png',
    'Branco': 'teclas/bran.png',
    'Corrigir': 'teclas/corr.png',
    'Confirmar': 'teclas/conf.png',
    'N': 'teclas/n.png',
}

buttons = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['N', '0', 'N'],
    ['Branco', 'Corrigir', 'Confirmar']
]

button_images = {}
button_size = (45, 45)

top_img = teclas(nums.get('top', 'teclas/top2.png'), size=(315, 130))
top_label = tk.Label(right_frame, image=top_img, bg='black')
top_label.image = top_img 
top_label.grid(row=0, column=0, columnspan=3, padx=0, pady=(47, 0), sticky="ew")
#padx é para os lados e pady é para cima e para baixo

for i, row in enumerate(buttons, start=1): 
    for j, button in enumerate(row):
        button_widget = tk.Button(right_frame, font=('Arial', 16), bd=0)
        if button != ' ':
            button_img = teclas(nums.get(button, 'teclas/default.png'), size=(100, 70))
            button_images[button] = button_img
        else:
            button_img = None
        
        if button_img:
            button_widget.config(image=button_img)
            button_widget.image = button_img 

        #button.bind("<Button-1>", tocar_som)

        button_widget.config(command = lambda k = button: press_key(k))

        button_widget.grid(row=i, column=j, padx=0, pady=0, sticky="nsew")

for i in range(6):
    right_frame.grid_rowconfigure(i, weight=0, minsize=30)
for j in range(3):
    right_frame.grid_columnconfigure(j, weight=0, minsize=30)


image_path_tela = 'tela.png'
desired_width_tela = 700
desired_height_tela = 490
tela_img = teclas(image_path_tela, size=(desired_width_tela, desired_height_tela))
tela_label = tk.Label(left_frame, image=tela_img, bg='white')
tela_label.image = tela_img 
tela_label.pack(side="top", fill="both", expand=True, padx=0, pady=10)


window.mainloop()