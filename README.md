# 👷‍♂️ Detecção de EPI (Equipamento de Proteção Individual) - YOLOv8n

Este projeto implementa um modelo de Detecção de Objetos (YOLOv8n) focado em detectar itens de segurança em canteiros de obras. O modelo foi treinado para reconhecer **11 classes** de EPI, incluindo capacetes, coletes, máscaras e, especificamente, óculos de proteção.

## 🌟 Resultados Finais do Modelo

O treinamento final foi interrompido na Época 99, apresentando o melhor desempenho nesse ponto.
* **Métrica de Desempenho (mAP50):** 0.82500 (ou 82.50%)
* **Épocas Concluídas:** 99

O modelo final (`best.pt`) está disponível na pasta de resultados.

---

## 💾 Fontes de Dados (Datasets)

O projeto usa a **fusão de dois datasets** públicos para garantir alta precisão, especialmente na detecção de óculos.

1.  **Dataset Principal (PPE de Construção - 10 Classes):**
    * **Fonte:** [Kaggle - Construction Site Safety Image Dataset (Roboflow)] (https://www.kaggle.com/datasets/snehilsanyal/construction-site-safety-image-dataset-roboflow)
    * **Classes Iniciais:** Hardhat, Mask, NO-Hardhat, NO-Mask, NO-Safety Vest, Person, Safety Cone, Safety Vest, machinery, vehicle.
    
2.  **Dataset Suplementar (Óculos - Goggle):** Um dataset separado do Roboflow focado apenas em óculos de proteção. https://universe.roboflow.com/safemind-onkro/glass-kuedh-qgclk/dataset/1
    * **Finalidade:** Foi usado para **aumentar a precisão** da classe Goggle e adicioná-la ao modelo base.

## ⚙️ Passo a Passo para Treinar e Usar (Instruções)

### A. Configuração do Ambiente

1.  **Instalar o Ambiente:** Certifique-se de ter o Anaconda/Miniconda instalado.
2.  **Criar/Ativar o Ambiente:** Ative o ambiente virtual `yolo` no Anaconda Prompt (Ex: `conda activate yolo`).
3.  **Instalar Ultralytics:** `pip install ultralytics`

### B. Preparação e Fusão dos Dados (Se for treinar do zero)

1.  **Estrutura de Pastas:** Os dois datasets (Principal e Óculos) foram combinados na pasta `css-data`, seguindo a estrutura `train/images`, `train/labels`, etc..
2.  **Re-Mapeamento de Classes:** O dataset de Óculos (Roboflow) usava um índice de classe diferente. O script **`remap.py`** foi executado para **mudar a classe 'Óculos' de 0 para 10** em todos os arquivos `.txt`.
    * *Comando:* `python remap.py`

### C. Treinamento

O Fine-Tuning foi realizado a partir de um modelo pré-treinado (`yolov8n.pt`) para as 11 classes, usando o arquivo de configuração **`ppe_glass_data.yaml`**.

1.  **Comando de Treinamento (Exemplo):**
    ```bash
    yolo train model=yolov8n.pt data="ppe_glass_data.yaml" epochs=150 imgsz=640 batch=4 project=./YOLO_RUNS_FUSION cache=False device=cpu
    ```
2.  **Para Retomar o Treinamento:** Se o treinamento for interrompido, utilize o *flag* `resume`:
    ```bash
    yolo train resume project=./YOLO_RUNS_FUSION
    ```

### D. Detecção/Uso do Modelo

Para usar o modelo treinado na webcam ou em um arquivo de vídeo:

1.  **Webcam:**
    ```bash
    yolo predict model=./YOLO_RUNS_FUSION/trainX/weights/best.pt source=0 device=cpu
    ```
2.  **Arquivo:**
    ```bash
    yolo predict model=./YOLO_RUNS_FUSION/trainX/weights/best.pt source="caminho/para/seu/video.mp4" device=cpu
    ```

**(Substitua `trainX` pelo nome correto da pasta de resultados dentro de `YOLO_RUNS_FUSION`)**
