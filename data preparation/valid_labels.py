import os
import shutil

# Paths
train_labels = "D:/UPC/Advanced Deep Learning/Assignment_2_project/dataset/labels/train"
valid_labels = "D:/UPC/Advanced Deep Learning/Assignment_2_project/dataset/labels/valid"
valid_images = "D:/UPC/Advanced Deep Learning/Assignment_2_project/dataset/images/valid"

os.makedirs(valid_labels, exist_ok=True)

# Get list of validation images (without extensions)
valid_image_names = {os.path.splitext(f)[0] for f in os.listdir(valid_images)}

# Move matching label files
for label_file in os.listdir(train_labels):
    file_name = os.path.splitext(label_file)[0]  # Remove extension
    if file_name in valid_image_names:
        shutil.move(os.path.join(train_labels, label_file),
                    os.path.join(valid_labels, label_file))

print("Validation labels moved successfully")
