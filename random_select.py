import os
import shutil
from random import sample


image_list = os.listdir("./images/")

for i in sample(range(len(image_list) - 1), 25):
    print(image_list[i])
    shutil.copy2(f'./images/{image_list[i]}', './training/')