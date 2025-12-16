👷‍♂️ Detecção de EPI (Equipamento de Proteção Individual) - YOLOv8nEste projeto implementa um modelo de Detecção de Objetos (**YOLOv8n**) focado em detectar itens de segurança em canteiros de obras. O modelo foi treinado para reconhecer **11 classes** de EPI.

---

###🌟 Resultados Finais do ModeloO treinamento final foi interrompido na Época 99, apresentando o melhor desempenho nesse ponto.

| Métrica | Valor |
| --- | --- |
| **mAP50** | **0.82500** (82.50%) |
| Épocas Concluídas | **99** |
| Modelo Final | `best.pt` (localizado no repositório) |

---

###💾 Fontes de Dados e PreparaçãoO projeto utiliza a **fusão de tres *datasets*** públicos, resultando em **12 classes** de detecção. O mapeamento das classes e o caminho dos dados estão definidos no arquivo **`ppe_glass_data.yaml`**.

####Processo de Preparação1. **Fusão e Estrutura:** Os *datasets* foram combinados em uma estrutura YOLOv8 (`train/images`, `valid/labels`, etc.) na pasta `css-data`.
2. **Mapeamento de Classes:** Foi realizado o remapeamento manual para garantir que a classe de `Glasses` (Óculos) fosse mapeada corretamente para o **ID 10** dentro do arquivo **`ppe_glass_data.yaml`**, resultando nas 11 classes finais.

| Detalhes do Dataset |
| --- |
| **Dataset Principal (PPE de Construção - 10 Classes):** Fonte: [Kaggle - Construction Site Safety Image Dataset (Roboflow)](https://www.google.com/search?q=https://universe.roboflow.com/testcasque/ppe-detection-qlq3d/dataset/1) |
| **Classe Adicional:** A classe de óculos foi incluída no ID `10` após a fusão dos dados. |
https://universe.roboflow.com/models/object-detection

---

###⚙️ Passo a Passo para Treinar e Usar (Instruções)####A. Configuração do Ambiente1. **Instalar/Ativar Ambiente:** Ative o ambiente virtual **`yolo`** no Anaconda Prompt.
```bash
conda activate yolo

```


2. **Instalar Ultralytics e Dependências:**
*(Você deve criar o arquivo `requirements.txt` com `pip install ultralytics` e outras bibliotecas necessárias)*
```bash
pip install -r requirements.txt

```



####B. TreinamentoO Fine-Tuning foi realizado a partir de um modelo pré-treinado (`yolov8n.pt`) para as **11 classes**.

* **Comando de Treinamento (Exemplo):**
```bash
yolo train model=yolov8n.pt data="ppe_glass_data.yaml" epochs=150 imgsz=640 batch=4 project=./results_yolov8n_100e/kaggle/working/runs/detect cache=False device=cpu

```


* **Para Retomar o Treinamento:** Utilize o *flag* `resume` e o caminho do seu projeto:
```bash
yolo train resume project=./results_yolov8n_100e/kaggle/working/runs/detect/train

```



####C. Detecção/Uso do Modelo (CLI)Para usar o modelo treinado (`best.pt`) na webcam ou em um arquivo de vídeo, aponte para o caminho do modelo e forneça o arquivo de configuração de classes.

* **Webcam (Detecção em Tempo Real):**
```bash
yolo predict model=./results_yolov8n_100e/kaggle/working/runs/detect/train/weights/best.pt source=0 data=ppe_glass_data.yaml

```


* **Arquivo de Vídeo/Imagem:**
```bash
yolo predict model=./results_yolov8n_100e/kaggle/working/runs/detect/train/weights/best.pt source="caminho/para/seu/arquivo.mp4" data=ppe_glass_data.yaml

```



---

Este README é o reflexo exato do que está no seu repositório agora!
