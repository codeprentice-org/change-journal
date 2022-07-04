# -*- coding: utf-8 -*-
import chunk
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
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
import dask.dataframe as dd


def create_dataframe(x,y):
    data=pd.DataFrame({"PSECT":x , 
                     "PMER":y})
    return data

x=np.random.normal(25,5,10000000)
y=np.random.normal(50,10,10000000)



data=create_dataframe(x,y)
dd_df=dd.from_pandas(data,chunksize=1000)
test_df=data.copy()
test_df["Total"]=test_df["PSECT"]+test_df["PMER"]
coordinates_1 = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]
coordinates_2=[(24.950899, 60.169158), (22.953492, 60.169158), (24.953510, 95.170104), (24.950958, 60.169990)]
poly_1 = Polygon(coordinates_1)
poly_2=Polygon(coordinates_2)
newdata = gpd.GeoDataFrame()
newdata.loc[0,"QSECT"]="NE"
newdata.loc[0,"PSECT"]=28
newdata.loc[0,"PTWP"]=68
newdata.loc[0,"PRGE"]=7
newdata.loc[0,"PMER"]=2
newdata.loc[0,"geometry"]=poly_1
newdata.loc[1,"QSECT"]="SE"
newdata.loc[1,"PSECT"]=28
newdata.loc[1,"PTWP"]=65
newdata.loc[1,"PRGE"]=6
newdata.loc[1,"PMER"]=2
newdata.loc[1,"geometry"]=poly_2
gis_data=newdata.set_crs(epsg=4326)


gdf=gpd.read_file('/home/ahnaf.ryan/data_download/SaskGrid_2015_QUARTERSECTION/SaskGrid_2015_QUARTERSECTION.shp')

gdf.head()

