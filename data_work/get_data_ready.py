from .size_manager import load_data
import data_work.data_info as di
import pandas as pd

def get_data_ready():
    return load_data(di.FILE_NAMES["small_file"])