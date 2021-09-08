import os
import shutil
from glob import glob
from random import sample


def copy_files():
    images_list = glob("./training_data/*.jpg")
    files_list = glob("./training_data/*.txt")
    images_list.sort()
    files_list.sort()

    val_dataset_idx = sample(range(len(images_list) - 1), 5)

    for idx in val_dataset_idx:
        shutil.copy2(images_list[idx], "./training_data/val/images/")
        shutil.copy2(files_list[idx], "./training_data/val/labels/")

    for image, file in zip(images_list, files_list):
        if images_list.index(image) not in val_dataset_idx and files_list.index(file) not in val_dataset_idx:
            shutil.copy2(image, "./training_data/train/images/")
            shutil.copy2(file, "./training_data/train/labels/")


if __name__ == "__main__":
    copy_files()