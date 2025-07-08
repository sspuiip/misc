import os
import numpy as np

dataset_dir = os.path.dirname(os.path.abspath(__file__))


def load_height_weight():
    file_path = dataset_dir + "/" + "height_weight.txt"
    ds=np.loadtxt(file_path)
    return ds