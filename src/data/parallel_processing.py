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
from sask_ndti_analysis.src.data.make_dataset import data## dummy dataframe

## Functions used for Task 1

def if_prime(x):
    if x <= 1:
        return 0
    elif x <= 3:
        return x
    elif x % 2 == 0 or x % 3 == 0:
        return 0
    i = 5
    while i**2 <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return 0
        i += 6
    return x

def df_func(df):
    value=df["PSECT"]*df["PMER"]
    value=round(value,ndigits=None)
    value=value.apply(func=if_prime)
    return value.sum()

def get_min_max(coordinates):
    latitude, longitude = [], []
    for i in coordinates:
        latitude.append(i[1])
        longitude.append(i[0])
    minimum, maximum = [], []
    minimum.append(min(longitude))
    minimum.append(min(latitude))
    maximum.append(max(longitude))
    maximum.append(max(latitude))
    wgs84 = minimum + maximum
    return wgs84


def get_boundary_box(df):
    #df=df.to_crs(epsg=4326)
    bbox = get_min_max(list(df.geometry.values[0].exterior.coords))
    return bbox



start=time.time()

iterative_mult_df=df_func(data)

end=time.time()

print(end-start) # 11.86 seconds

## multiprocessing

start=time.time()

def get_data(df,func,n_split=1000):
    df_split=np.array_split(df,n_split)
    n_cores=multiprocessing.cpu_count()
    pool=Pool(2)
    df=sum(pool.map(func,df_split))
    pool.close()
    pool.join()
    return df

multiproc_mult_df=get_data(data,df_func)
print(multiproc_mult_df)
end=time.time()
print(end-start)






