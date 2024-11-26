import pygame

pygame.mixer.init()

def testar_som():
    try:
        pygame.mixer.music.load('D:/bip.mp3')  # Caminho do arquivo .wav
        pygame.mixer.music.play()
        print("Som está tocando.")
        while pygame.mixer.music.get_busy():  # Aguarda até que o som termine
            pygame.time.Clock().tick(10)
    except pygame.error as e:
        print(f"Erro ao carregar o som: {e}")

testar_som()