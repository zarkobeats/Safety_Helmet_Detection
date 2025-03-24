# Safety Helmet Detection using YOLOv5s and Kaggle Dataset

This project implements a Safety Helmet Detection system using the YOLOv5s model. The dataset is sourced from Kaggle and processed for training and evaluation. The model is trained to detect helmets in both images and videos.

## Prerequisites

- PyTorch and Torchvision installed
- Kaggle API for dataset download
- Additional libraries specified in `requirements.txt`

## Table of Contents
- [Installation](#installation)
- [Dataset Preparation](#dataset-preparation)
- [Training the Model](#training-the-model)
- [Inference](#inference)
- [Evaluation](#evaluation)
- [Testing on Unseen Data](#testing-on-unseen-data)
- [Results](#results)
- [Acknowledgments](#acknowledgments)

---

## Installation

To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

Clone the YOLOv5 repository and place the custom yaml script for helmet detection, called `helmet_dataset.yaml` in `\yolov5\data` :
```bash
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
```

---

## Dataset Preparation

1. **Download the Dataset:**
   - Use `download.py` to download the dataset from Kaggle. URL: https://www.kaggle.com/datasets/andrewmvd/hard-hat-detection

2. **Split Training and Validation Sets:**
   - Run `split_train_and_valid.py` to split the images and annotations into training and validation sets under the `dataset/images and dataset/annotations` folder.

3. **Convert Annotations to YOLO Format:**
   - Use `xml_to_yolo.py` to convert XML annotations to YOLO format and save them in `dataset/labels/train`.

4. **Validate Labels:**
   - Use `valid_labels.py` to take testing labels from `dataset/labels/train`, that correspond to the images from the `dataset/images/valid` and place these testing labels in `dataset/labels/valid`.

---

## Training the Model

### First Training Run (Image Size: 640x640)
```bash
python train.py --img 640 --batch 8 --epochs 50 --data data/helmet_dataset.yaml --weights yolov5s.pt --device cpu --workers 2
```

### Second Training Run (Image Size: 960x960)
```bash
python train.py --img 960 --batch 8 --epochs 50 --data data/helmet_dataset.yaml --weights yolov5s.pt --device cpu --workers 2
```

---

## Inference

### Detection on Validation Set
- **Image Size 640x640:**
```bash
python detect.py --weights runs/train/exp7/weights/best.pt --img 640 --source "D:/UPC/Advanced Deep Learning/Assignment_2_project/dataset/images/valid" --save-txt --save-conf
```

- **Image Size 960x960:**
```bash
python detect.py --weights runs/train/exp8/weights/best.pt --img 960 --source "D:/UPC/Advanced Deep Learning/Assignment_2_project/dataset/images/valid" --save-txt --save-conf
```

---

## Evaluation

### Validation Metrics
- **Image Size 640x640:**
```bash
python val.py --weights runs/train/exp7/weights/best.pt --data data/helmet_dataset.yaml --img 640
```

- **Image Size 960x960:**
```bash
python val.py --weights runs/train/exp8/weights/best.pt --data data/helmet_dataset.yaml --img 960
```

---

## Testing on Unseen Data

### On Images
- **640x640:**
```bash
python detect.py --weights runs/train/exp7/weights/best.pt --img 640 --source "D:/UPC/Advanced Deep Learning/Assignment_2_project/unseen_media/images" --save-txt --save-conf
```

- **960x960:**
```bash
python detect.py --weights runs/train/exp8/weights/best.pt --img 960 --source "D:/UPC/Advanced Deep Learning/Assignment_2_project/unseen_media/images" --save-txt --save-conf
```

### On Videos
- **640x640:**
```bash
python detect.py --weights runs/train/exp7/weights/best.pt --img 640 --source "D:/UPC/Advanced Deep Learning/Assignment_2_project/unseen_media/videos/"
```

- **960x960:**
```bash
python detect.py --weights runs/train/exp8/weights/best.pt --img 960 --source "D:/UPC/Advanced Deep Learning/Assignment_2_project/unseen_media/videos/"
```

---

## Results
Visual results(matrices and curves) could be found in the `evaluation` folder in the corresponding folder for both image sizes. Images and videos with the detection squares can be found in the folder `results` corresponding folder for both image sizes.

---

## Acknowledgments
- [YOLOv5 by Ultralytics](https://github.com/ultralytics/yolov5)
- Safety Helmet Detection from Kaggle by andrewmvd

