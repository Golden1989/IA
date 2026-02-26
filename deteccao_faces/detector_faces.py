import cv2
import os
import matplotlib.pyplot as plt

# Mostrar diretório atual
print(f"Diretório atual: {os.getcwd()}")

# Caminhos das pastas (versão mais robusta)
caminho_base = os.path.dirname(os.path.abspath(__file__))
caminho_imagens = os.path.join(caminho_base, "imagens")
caminho_modelo = os.path.join(caminho_base, "modelos")

print(f"Procurando imagens em: {caminho_imagens}")
print(f"Procurando modelo em: {caminho_modelo}")

# Verificar se as pastas existem
if not os.path.exists(caminho_imagens):
    print(f"ERRO: Pasta {caminho_imagens} não existe!")
    exit()

if not os.path.exists(caminho_modelo):
    print(f"ERRO: Pasta {caminho_modelo} não existe!")
    exit()

# Carregar o classificador
modelo_path = os.path.join(caminho_modelo, 'haarcascade_frontalface_default.xml')
if not os.path.exists(modelo_path):
    print(f"ERRO: Arquivo {modelo_path} não encontrado!")
    exit()

classifier = cv2.CascadeClassifier(modelo_path)

# Listar imagens na pasta
imagens_teste = ['test1.jpg', 'test2.jpg']

for nome_arquivo in imagens_teste:
    caminho_completo = os.path.join(caminho_imagens, nome_arquivo)
    print(f"Tentando abrir: {caminho_completo}")
    
    imagem = cv2.imread(caminho_completo)
    
    if imagem is None:
        print(f"ERRO: Não foi possível carregar {caminho_completo}")
        # Listar arquivos na pasta imagens para debug
        print(f"Arquivos em {caminho_imagens}: {os.listdir(caminho_imagens)}")
        continue
    
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(imagem, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
    
    print(f"{nome_arquivo}: {len(faces)} face(s) detectada(s)")
    
    # Mostrar com matplotlib
    imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(10, 8))
    plt.imshow(imagem_rgb)
    plt.title(f'{nome_arquivo} - {len(faces)} faces detectadas')
    plt.axis('off')
    plt.show()

print("Processamento concluído!")