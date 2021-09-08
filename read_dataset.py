import pdfkit
from tqdm import tqdm
from multiprocessing import cpu_count
from joblib import Parallel, delayed


def download_from_url(url, destination):
    print(url)
    try:
        pdfkit.from_url(url, destination)
    except Exception as e:
        print(str(e))



if __name__ == "__main__":
    with open("structure-detection-data-set.txt", 'r') as f:
        dataset_list = f.readlines()

    executor = Parallel(n_jobs=cpu_count(), backend='multiprocessing')
    tasks = (delayed(download_from_url)(url, f'./pdf_files/{i+1}.pdf') for i, url in enumerate(dataset_list))
    response = executor(tasks)
