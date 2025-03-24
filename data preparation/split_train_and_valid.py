import os
import random
import shutil

# Paths
dataset_path = "D:/UPC/Advanced Deep Learning/Assignment_2_project/dataset"
image_path = os.path.join(dataset_path, "images")
annotation_path = os.path.join(dataset_path, "annotations")

# New folders
train_img_dir = os.path.join(dataset_path, "images/train")
valid_img_dir = os.path.join(dataset_path, "images/valid")
train_label_dir = os.path.join(dataset_path, "labels/train")
valid_label_dir = os.path.join(dataset_path, "labels/valid")

for d in [train_img_dir, valid_img_dir, train_label_dir, valid_label_dir]:
    os.makedirs(d, exist_ok=True)

# Get all images
images = [f for f in os.listdir(
    image_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
random.shuffle(images)

# 80% train, 20% valid
split_idx = int(len(images) * 0.8)
train_images = images[:split_idx]
valid_images = images[split_idx:]

# Move images and annotations
for img in train_images:
    shutil.move(os.path.join(image_path, img),
                os.path.join(train_img_dir, img))
    annotation = os.path.splitext(img)[0] + ".txt"
    if os.path.exists(os.path.join(annotation_path, annotation)):
        shutil.move(os.path.join(annotation_path, annotation),
                    os.path.join(train_label_dir, annotation))

for img in valid_images:
    shutil.move(os.path.join(image_path, img),
                os.path.join(valid_img_dir, img))
    annotation = os.path.splitext(img)[0] + ".txt"
    if os.path.exists(os.path.join(annotation_path, annotation)):
        shutil.move(os.path.join(annotation_path, annotation),
                    os.path.join(valid_label_dir, annotation))

print("Dataset split into train and valid")
