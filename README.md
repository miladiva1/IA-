👷‍♂️ PPE (Personal Protective Equipment) Detection - YOLOv8nThis project implements an Object Detection model (**YOLOv8n**) focused on detecting safety items in construction sites. The model was trained to recognize **11 classes** of PPE.

---

###🌟 Final Model ResultsThe final training was stopped at Epoch 99, showing the best performance at that point.

| Metric | Value |
| --- | --- |
| **mAP50** | **0.82500** (82.50%) |
| Epochs Completed | **99** |
| Final Model | `best.pt` (located in the repository) |

---

###💾 Data Sources and PreparationThe project uses the **fusion of three public datasets**, resulting in **11 classes** of detection. The class mapping and data path are defined in the **`ppe_glass_data.yaml`** file.

####Preparation Process1. **Fusion and Structure:** The datasets were combined into a YOLOv8 structure (`train/images`, `valid/labels`, etc.) in the `css-data` folder.
2. **Class Mapping:** Manual remapping was performed to ensure the `Glasses` class was correctly mapped to **ID 10** within the **`ppe_glass_data.yaml`** file, resulting in the 11 final classes.

| Dataset Details |
| --- |
| **Main Dataset (Construction PPE - 10 Classes):** Source: [Kaggle - Construction Site Safety Image Dataset (Roboflow)](https://www.kaggle.com/datasets/snehilsanyal/construction-site-safety-image-dataset-roboflow) |
| **Additional Data Sources (Used for Glasses and Gloves):** [Roboflow - glass-kuedh](https://universe.roboflow.com/v2-tc2ax/glass-kuedh), [Roboflow - gloves-gzbgu](https://universe.roboflow.com/work-dvvvh/gloves-gzbgu). |
| **Final Classes:** The final classes included `Glasses` (mapped to ID 10) and the original 10 classes, totaling **11 classes**. |

---

###⚙️ Step-by-Step Guide for Training and Usage (Instructions)####A. Environment Setup1. **Install/Activate Environment:** Activate the **`yolo`** virtual environment in the Anaconda Prompt.
```bash
conda activate yolo

```


2. **Install Ultralytics and Dependencies:**
*(You must create the `requirements.txt` file with `pip install ultralytics` and other necessary libraries)*
```bash
pip install -r requirements.txt

```



####B. TrainingFine-Tuning was performed starting from a pre-trained model (`yolov8n.pt`) for the **11 classes**.

* **Training Command (Example):**
```bash
yolo train model=yolov8n.pt data="ppe_glass_data.yaml" epochs=150 imgsz=640 batch=4 project=./results_yolov8n_100e/kaggle/working/runs/detect cache=False device=cpu

```


* **To Resume Training:** Use the `resume` flag and the path to your project:
```bash
yolo train resume project=./results_yolov8n_100e/kaggle/working/runs/detect/train

```



####C. Detection/Model Usage (CLI)To use the trained model (`best.pt`) on a webcam or a video file, point to the model path and provide the class configuration file.

* **Webcam (Real-Time Detection):**
```bash
yolo predict model=./results_yolov8n_100e/kaggle/working/runs/detect/train/weights/best.pt source=0 data=ppe_glass_data.yaml

```


* **Video/Image File:**
```bash
yolo predict model=./results_yolov8n_100e/kaggle/working/runs/detect/train/weights/best.pt source="path/to/your/file.mp4" data=ppe_glass_data.yaml

```



---



---


