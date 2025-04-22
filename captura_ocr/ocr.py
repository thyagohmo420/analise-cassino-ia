import cv2
import pytesseract
import pyautogui
from datetime import datetime

def capturar_print(nome_arquivo="dados/ultima_captura.png"):
    screenshot = pyautogui.screenshot()
    screenshot.save(nome_arquivo)
    return nome_arquivo

def extrair_numero(caminho_imagem):
    img = cv2.imread(caminho_imagem)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numero = pytesseract.image_to_string(gray, config='--psm 8 digits')
    return numero.strip()

if __name__ == "__main__":
    caminho = capturar_print()
    numero = extrair_numero(caminho)
    print(f"Número identificado: {numero} - {datetime.now()}")