# 🤖 Projetos de IA

Este repositório será dedicado a projetos relacionados com **Inteligência Artificial**.  
O objetivo é aprender, experimentar e aplicar técnicas de IA em diferentes contextos, incluindo possíveis usos em **Cibersegurança** no futuro.

---

## 📌 Projeto 1 — Welcome Task
O primeiro projeto deste repositório é chamado **Welcome Task**.  

A proposta era ensinar uma IA a reconhecer **uma pessoa, objeto, personagem ou animal**.  
A pessoa escolhida por mim foi a **Taylor Swift** 🎤.

### 🔗 Recursos
- [📂 Google Drive](https://drive.google.com/drive/folders/1AS5CHH_fJ75dSbYYZCwSWt_teaIj9wMm?usp=sharing) — pastas de **validação** e **teste** com imagens utilizadas.  
- [🎥 YouTube](https://www.youtube.com/shorts/p9gPYFBxExo) — vídeo usado para extrair frames para treinamento.  
- [💻 Google Colab](https://colab.research.google.com/drive/1NDAIrlHLugOiHpTQAK96nCZsWFf-FqLI?usp=sharing) — notebook com o código completo do treinamento.  

---

## 🎯 Aplicação em Cibersegurança

Embora o **Welcome Task** seja um projeto simples de reconhecimento facial, ele traz ideias que podem ser aplicadas em contextos de **cibersegurança e investigação digital**.  

Uma possibilidade seria o uso de **fontes abertas (OSINT)**.  
Por exemplo: utilizando ferramentas que coletam imagens públicas de redes sociais (como Instagram), é possível criar um dataset de fotos de um **suspeito ou criminoso**.  
Essas imagens poderiam ser usadas para treinar uma IA de reconhecimento facial que:  

- Identifique automaticamente o indivíduo em **câmeras de segurança públicas ou privadas**;  
- Monitore entradas de prédios, estabelecimentos ou residências;  
- Seja aplicada até em sistemas caseiros de segurança, caso o usuário possua câmeras conectadas.  

👉 Assim, a ideia inicial de reconhecer uma celebridade (Taylor Swift) serve como **base prática** para aplicações mais sérias em **segurança pública e digital**.  

---

## 📌 Projeto 2 — Assistente de Cibersegurança com IA

Este projeto foi desenvolvido em **Python** no **Google Colab**, utilizando o **Groq LLM** para criar um assistente inteligente voltado à **cibersegurança**.

A ideia foi ensinar a IA a **identificar falhas de segurança** em exemplos simulados, como:
- 🔍 **Portas TCP abertas** — a IA consegue reconhecer portas vulneráveis a partir de uma lista de strings e sugere ações para fechá-las.  
- ⏱️ **Análise de logs** — identifica acessos fora do horário comercial e indica que o acesso deve ser bloqueado.  
- 🚫 **Controle de acesso** — a lógica de corte está implementada, mas como o Colab não permite automação direta, as ações são **simuladas**.  

### 🛠️ Tecnologias
- Python (Google Colab)  
- Groq LLM  
- Scripts para análise de portas e logs

## 🚀 Como Executar
1. Abra o [notebook no Google Colab](https://colab.research.google.com/drive/1OLW49HTNp1YbF7lFUzhgjsY4nE9M-hVM#scrollTo=HcihFKNnQxBR).  
2. Execute as células para carregar as dependências e inicializar o modelo.  
3. Teste com a lista de portas e logs fornecidos para simular cenários de segurança.

### 🎯 Aplicações
Este projeto mostra como a IA pode ser aplicada em **cibersegurança**, servindo de base para:  
- Detecção de vulnerabilidades em redes;  
- Apoio a sistemas de monitoramento e resposta a incidentes;  
- Automação de tarefas de segurança.  

### 🚀 Próximos Passos
- Implementar a automação fora do Colab, rodando em ambiente real;  
- Ampliar a análise de logs com técnicas de **Machine Learning** para anomalias;  
- Integrar a solução com monitoramento em tempo real.

---

## 📌 Projeto 3 — Detecção de Faces com OpenCV (TCC)

Este é o projeto mais recente, desenvolvido como parte do meu **Trabalho de Conclusão de Curso (TCC)** em Cibersegurança.

### 🎯 Objetivo

O sistema carrega imagens, detecta rostos utilizando o classificador **Haar Cascade** do OpenCV e exibe as imagens com as faces demarcadas por retângulos verdes. Este é o primeiro passo para um sistema mais complexo de **reconhecimento facial** voltado para segurança em ambientes universitários.

### 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **OpenCV (cv2)** — processamento de imagens
- **Matplotlib** — exibição gráfica

### 📁 Estrutura

deteccao_faces/
├── detector_faces.py # Script principal
├── imagens/ # Imagens para teste
├── modelos/ # Classificador Haar Cascade
└── README.md # Documentação completa


### 🔍 Funcionalidades

- Leitura de imagens da pasta `imagens/`
- Detecção de faces com o algoritmo Haar Cascade
- Visualização com retângulos verdes nas faces detectadas
- Feedback no terminal com o número de faces encontradas

### 🚀 Como Executar

  '''bash
    cd deteccao_faces
    python3 -m venv venv
    source venv/bin/activate  # Linux/Mac
    pip install opencv-python matplotlib
    python detector_faces.py 

---

## 🔮 Próximos Passos
- Adicionar novos projetos de IA;  
- Criar experimentos voltados especificamente para **Cibersegurança**;  
- Explorar técnicas de detecção, automação e análise aplicadas a segurança.  

---

## ✨ Autor
Desenvolvido por **Golden1989**  

