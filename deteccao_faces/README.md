# 🕵️‍♀️ Detecção de Faces com OpenCV

Este projeto faz parte do meu Trabalho de Conclusão de Curso (TCC) em Cibersegurança e tem como objetivo detectar faces em imagens usando o classificador **Haar Cascade** do OpenCV.

## 📌 Sobre o Projeto

O sistema carrega imagens de uma pasta, detecta rostos utilizando o modelo pré-treinado `haarcascade_frontalface_default.xml` e exibe as imagens com as faces demarcadas por retângulos verdes. Este é o primeiro passo para um sistema mais complexo de **reconhecimento facial** voltado para segurança em ambientes universitários.

### 🎯 Funcionalidades do Código

- **Leitura de imagens**: O script carrega imagens da pasta `imagens/`
- **Detecção de faces**: Utiliza o algoritmo Haar Cascade para localizar rostos
- **Visualização**: Desenha retângulos verdes ao redor das faces detectadas
- **Exibição**: Mostra os resultados usando matplotlib (mais estável que a interface nativa do OpenCV)
- **Feedback**: Exibe no terminal quantas faces foram encontradas em cada imagem

## 🛠️ Tecnologias Utilizadas

- **Python 3.12** - Linguagem base do projeto
- **OpenCV (cv2)** - Biblioteca de visão computacional para processamento de imagens
- **Matplotlib** - Biblioteca para exibição gráfica das imagens

## 📁 Estrutura do Projeto
deteccao_faces/
│
├── detector_faces.py # Script principal com o código de detecção
├── README.md # Este arquivo de documentação
│
├── imagens/ # Pasta com as imagens para teste
│ ├── test1.jpg # Imagem com 2 pessoas
│ └── test2.jpg # Imagem com múltiplas pessoas
│
├── modelos/ # Modelos pré-treinados
│ └── haarcascade_frontalface_default.xml # Classificador Haar Cascade para faces frontais
│
└── venv/ # Ambiente virtual (não incluso no repositório)
└── ... # Será criado localmente


## 🚀 Como Configurar e Executar

Siga os passos abaixo para rodar o projeto no seu computador:

### Pré-requisitos

- Python 3.8 ou superior instalado
- Git instalado (opcional, para clonar)

### Passo a Passo

1. **Clone o repositório** (ou baixe os arquivos)
   ```bash
   git clone https://github.com/Golden1989/IA.git
   cd IA/deteccao_faces
2.Crie um ambiente virtual (recomendado para isolar as dependências)
    bash
  
  python3 -m venv venv

3.Ative o ambiente virtual

  No Linux/Mac:
  bash
  
  source venv/bin/activate
  
  No Windows:
  bash
  
  venv\Scripts\activate

  Você saberá que funcionou quando aparecer (venv) no início da linha do terminal.

4.Instale as dependências
  bash
  
  pip install opencv-python matplotlib

5.Execute o projeto
  bash
  
  python detector_faces.py

📸 Resultados Esperados

Ao executar o script, você verá:

    No terminal: mensagens indicando quantas faces foram detectadas em cada imagem

    Janelas do matplotlib: imagens com retângulos verdes ao redor das faces

    Pressione qualquer tecla para fechar cada imagem e ver a próxima
Exemplo de saída no terminal:
test1.jpg: 2 face(s) detectada(s)
test2.jpg: 15 face(s) detectada(s)
Processamento concluído!

⚠️ Observações Importantes

    O ambiente virtual (venv/) não deve ser enviado ao GitHub (já está no .gitignore)

    As bibliotecas instaladas podem variar conforme o sistema operacional

    Em alguns sistemas Linux, pode ser necessário instalar o python3-tk para o matplotlib funcionar:
    bash

    sudo apt install python3-tk
  

📄 Licença

Este projeto está sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
