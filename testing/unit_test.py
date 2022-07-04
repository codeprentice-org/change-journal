from timeit import timeit
from tkinter import NE
import pandas as pd
import pytest
import multiprocessing 
import numpy as np
from multiprocessing import Pool
import random
from functools import reduce
import time
import geopandas as gpd
from shapely.geometry import Point, Polygon
from sentinelhub import *
import os
import json
from functools import wraps
import pytest


import sys
import os


os.getcwd()

os.chdir('/home/ahnaf.ryan/datascience work/sask_ndti_analysis/sask_ndti_analysis')

os.getcwd()


import sys
import os

sys.path.append("/home/ahnaf.ryan/datascience work/sask_ndti_analysis/sask_ndti_analysis/src/data")  
from sask_ndti_analysis.src.data import get_rs_data


def test_config_instance_id():
    assert get_rs_data.get_config().instance_id=="41eea464-76bb-4ae8-ae76-eb84232640a5"
    
def test_len_config_instance_id():
    assert len(get_rs_data.get_config().instance_id)==36
    
def test_config_client_id():
    assert get_rs_data.get_config().sh_client_id=="f668a789-e9c0-4a61-8c25-b48cc8bbaccf"
    
def test_len_config_client_id():
    assert len(get_rs_data.get_config().sh_client_id)==36

def test_config_client_secret():
    assert get_rs_data.get_config().sh_client_secret=="m7{7![TbVZcEbg3]:CMqjU4r6Qh%Gd5|n|O4UTwp"
    
def test_len_config_client_secret():
    assert len(get_rs_data.get_config().sh_client_secret)==40
 
 
## just playing around 
x=get_rs_data.save_sh_LETM2_data(get_rs_data.save_LETM2_ndvi(layer='NDVI',
                   bbox=[],
                   start_date= "2002-01-01",
                   end_date="2021-12-31",
                   output_folder="",
                   config=get_rs_data.get_config()))
 
 
    
    
#python -m pytest sask_ndti_analysis/testing/unit_test.py




    

