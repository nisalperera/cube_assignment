from multiprocessing import cpu_count
from joblib import Parallel, delayed
from pdf2image import convert_from_path
from glob import glob
from random import randint


def convert_save(pdf_file):
    print(pdf_file)
    filename = pdf_file.split("/")[-1].split(".")[0]
    images = convert_from_path(pdf_file)
    for _ in range(2):
        i = randint(0, len(images) - 1)
        images[i].save('./images/' + filename + "_" + str(i) + '.jpg', 'JPEG')
 

if __name__ == "__main__":

    pdf_files_list = glob("./pdf_files/*.pdf")
    pdf_files_list.sort()

    # executor = Parallel(n_jobs=2, backend='multiprocessing')
    # tasks = (delayed(convert_save)(file) for file in pdf_files_list)
    # response = executor(tasks)
    for file in pdf_files_list:
        convert_save(file)