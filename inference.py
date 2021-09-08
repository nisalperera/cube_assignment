import os
import torch
import argparse
from random import sample
from glob import glob
from PIL import Image, ImageDraw
from tqdm import tqdm


@torch.no_grad()
def inference(model, image_paths: list, classes: list):

    print("Performing Inference...")
    for image_path in tqdm(image_paths):
        image = Image.open(image_path)
        results = model(image, size=1024).pandas().xyxy[0].to_numpy()

        drawImage = ImageDraw.Draw(image)

        for result in results:
            x1, y1, x2, y2 = results[:4]
            class_name = classes[result[5]]
            drawImage.rectangle([(x1, y1, x2, y2)], outline="#90EE90")
            drawImage.text((x1, y1), class_name)

        image.save(os.path.join("inference_results", image_path.split("/")[1]))

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model-path', default='./models/exp5/weights/best.pt')
    parser.add_argument('-c', '--class-file', default='./training_data/classes.txt')
    parser.add_argument('-t', '--test-images', default='images/')
    args = parser.parse_args()

    device = None

    if torch.cuda.is_available():
        device = 'cuda'
    else:
        device = 'cpu'

    with open(args.class_file, "r") as f:
        classes = [class_name.rstrip() for class_name in f.readlines()]
        f.close()
    # print(classes)

    product_detector = torch.hub.load('ultralytics/yolov5', 'custom', 
                        path=args.model_path, 
                        force_reload=True, device=device)
    product_detector.eval()

    image_paths_list = sorted(glob(os.path.join(args.test_images, "*.jpg")))
    image_paths_list = [image_paths_list[i] for i in sample(range(len(image_paths_list)), 20)]

    inference(product_detector, image_paths_list, classes)