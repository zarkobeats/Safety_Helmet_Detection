import os
import xml.etree.ElementTree as ET

# Paths
input_folder = r"D:\UPC\Advanced Deep Learning\Assignment_2_project\dataset\annotations"
output_folder = r"D:\UPC\Advanced Deep Learning\Assignment_2_project\dataset\labels\train"

os.makedirs(output_folder, exist_ok=True)

# Class mapping
class_mapping = {"helmet": 0, "person": 1, "head": 2}

# Function to convert XML to YOLO format


def convert_xml_to_yolo(xml_path, output_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    width = int(root.find("size/width").text)
    height = int(root.find("size/height").text)

    yolo_lines = []

    for obj in root.findall("object"):
        class_name = obj.find("name").text
        if class_name not in class_mapping:
            continue

        class_id = class_mapping[class_name]
        bbox = obj.find("bndbox")

        xmin = int(bbox.find("xmin").text)
        ymin = int(bbox.find("ymin").text)
        xmax = int(bbox.find("xmax").text)
        ymax = int(bbox.find("ymax").text)

        x_center = (xmin + xmax) / (2 * width)
        y_center = (ymin + ymax) / (2 * height)
        bbox_width = (xmax - xmin) / width
        bbox_height = (ymax - ymin) / height

        yolo_lines.append(
            f"{class_id} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}")

    with open(output_path, "w") as f:
        f.write("\n".join(yolo_lines))


# Process all XML files
for filename in os.listdir(input_folder):
    if filename.endswith(".xml"):
        xml_path = os.path.join(input_folder, filename)
        txt_filename = os.path.splitext(filename)[0] + ".txt"
        output_path = os.path.join(output_folder, txt_filename)
        convert_xml_to_yolo(xml_path, output_path)

print("Conversion completed.")
