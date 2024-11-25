import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

input_number = ""

# Funcao teste antes de importar eleicao_ar
def get_candidato_info(candidato_number):
    candidatos = {
        '93': {
            'nome': 'Andressa Urach',
            'partido': 'Jacaré',
            'vice': 'Marido da Lana Del Rey',
            'image': 'D:/urna ferrauche/andressa.png',  
            'vice_image': 'D:/urna ferrauche/marido_lana.png' 
        }
    }
    return candidatos.get(candidato_number, None)

def press_key(key):
    global input_number  
    if key == 'Confirmar':
            ve_imagem()
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
        img = Image.open("D:/urna ferrauche/justica_eleitoral.png")
        img = img.resize((int(img.width * 0.65), int(img.height * 1.3)), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        
        img_label.config(image=img)
        img_label.image = img
    except Exception as e:
        print("Erro ao carregar a imagem:", e)
        return

def ver_candidato_info(candidato_number):
    candidato_info = get_candidato_info(candidato_number)
    
    if candidato_info:
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
    else:
        candidato_label.config(text="Candidato não encontrado!")

window = tk.Tk()
window.title("Urna eletrônica")
window.geometry("1100x1100")  
window.configure(bg='black')

# Frames para layout
left_frame = tk.Frame(window, bg='white')
left_frame.pack(side="left", fill="y", padx=20, pady=20) 
right_frame = tk.Frame(window, bg='black')
right_frame.pack(side="right", fill="y", padx=20, pady=20)

img_label = tk.Label(left_frame, bg='black')
img_label.pack(side="top", padx=10, pady=20)  

candidato_label = tk.Label(left_frame, bg='white', fg='black', font=('Arial', 16), justify="left")
candidato_label.pack(side="top", padx=10, pady=20)

candidato_image_label = tk.Label(left_frame)
candidato_image_label.place(relx=0.5, rely=0.4, anchor='n') 
vice_image_label = tk.Label(left_frame)
vice_image_label.place(relx=0.5, rely=0.6, anchor='n')  

buttons = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    [' ', '0', ' '],
    ['Branco', 'Corrigir', 'Confirmar']
]

for i, row in enumerate(buttons):
    for j, button in enumerate(row):
        bg_color = 'black'
        fg_color = 'white'
        
        if button == 'Branco':
            bg_color = 'white'
            fg_color = 'black'
        elif button == 'Corrigir':
            bg_color = 'red'
            fg_color = 'white'
        elif button == 'Confirmar':
            bg_color = 'green'
            fg_color = 'white'
        
        tk.Button(right_frame, text=button, width=10, height=4, bg=bg_color, fg=fg_color, font=('Arial', 16),
                  command=lambda key=button: press_key(key)).grid(row=i, column=j, padx=5, pady=5)

window.mainloop()
