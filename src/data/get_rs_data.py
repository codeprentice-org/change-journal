import pandas as pd
import numpy as np
import geopandas as gpd
from sentinelhub import *
import os
import json
import datetime
from functools import wraps

## under src, create a dataset, 

## reading the shape file, downloading the soil data, fetch this remote sensing, centinnel hub, 
 
## read the lld from the shape file, process multiple rows of the dataframe, 10000 rows, 1000 rows at a time, each of the 1000 rows, execute a function in parallel, justify my method

## create a function get_data(1000 rows of data)
start_year = '2002'
end_year = '2021'

period_start = '04-14'
period_end = '05-14'

def get_lld_bounding_box(qsect, psect, township, range, meridian):
    pass


def get_config():
    sh_config = SHConfig()
    sh_config.instance_id = '41eea464-76bb-4ae8-ae76-eb84232640a5'
    sh_config.sh_client_id = 'f668a789-e9c0-4a61-8c25-b48cc8bbaccf'
    sh_config.sh_client_secret = 'm7{7![TbVZcEbg3]:CMqjU4r6Qh%Gd5|n|O4UTwp'
    return sh_config




def save_sh_LETM2_data(func):
    @wraps(func)
    def wrapped(*args, **kwargs): 
        request = WcsRequest(
            data_collection=DataCollection.LANDSAT_ETM_L2,
            layer=kwargs['layer'],
            bbox=BBox(bbox=kwargs['bbox'], crs=CRS.WGS84),
            image_format=MimeType.TIFF,
            time=(kwargs['start_date'], kwargs['end_date']),
            time_difference = datetime.timedelta(hours=2),
            resx='30m',
            resy='30m',
            data_folder=kwargs['output_folder'],
            config=kwargs['config'])
        request.save_data()
        return None
    return wrapped

def get_min_max(coordinates):
    if coordinates==[]:
        raise Exception("Sorry, Coordinate is empty!")
    else:
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
    



@save_sh_LETM2_data
def save_LETM2_ndvi(layer: str='NDVI',
                   bbox:list=[],
                   start_date:str = "2002-01-01",
                   end_date="2021-12-31",
                   output_folder: str="",
                   config=None):
    return {'layer':layer,
            'bbox':bbox,
            'start_date':start_date,
            'end_date': end_date,
            output_folder: output_folder,
            config: config}

@save_sh_LETM2_data
def save_LETM2_data(layer: str='NDTI',
                   bbox:list=[],
                   start_date:str = "2002-01-01",
                   end_date="2021-12-31",
                   output_folder: str="",
                   config=None):
    return {'layer':layer,
            'bbox':bbox,
            'start_date':start_date,
            'end_date': end_date,
            output_folder: output_folder,
            config: config}

def save_data_for_periods(start_dates = [],
                          end_dates=[],
                          layer: str=None,
                          bbox=None, 
                          output_folder: str=None, 
                          config=None):
    for (st_dt, end_dt) in zip(start_dates, end_dates):
        save_LETM2_data(layer=layer,
                        bbox=bbox,
                        start_date=st_dt,
                        end_date=end_dt,
                        output_folder=output_folder,
                        config=config)

def get_boundary_box(QSECT: str = None,
                     PSECT: str = None,
                     PTWP: str = None,
                     PRGE: str = None,
                     PMER: str = None,file_path: str= None,gdf:gpd.GeoDataFrame=None):
    if gdf is None:
        sasketchwan_gpd = gpd.read_file(file_path)
        sasketchwan_gpd_WGS84 = sasketchwan_gpd.to_crs(4326)
        temp = sasketchwan_gpd_WGS84[(sasketchwan_gpd_WGS84.QSECT==QSECT) & (sasketchwan_gpd_WGS84.PSECT==PSECT) & (sasketchwan_gpd_WGS84.PTWP==PTWP) & (sasketchwan_gpd_WGS84.PRGE==PRGE) & (sasketchwan_gpd_WGS84.PMER==PMER)]
        if temp.empty==True:
                raise Exception("Sorry, Dataframe is empty!")
        else:
            bbox = get_min_max(list(temp.geometry.values[0].exterior.coords))
            return bbox
    else:
        sasketchwan_gpd_WGS84 = gdf.to_crs(4326)
        temp = sasketchwan_gpd_WGS84[(sasketchwan_gpd_WGS84.QSECT==QSECT) & (sasketchwan_gpd_WGS84.PSECT==PSECT) & (sasketchwan_gpd_WGS84.PTWP==PTWP) & (sasketchwan_gpd_WGS84.PRGE==PRGE) & (sasketchwan_gpd_WGS84.PMER==PMER)]
        if temp.empty==True:
                raise Exception("Sorry, Dataframe is empty!")
        else:
            bbox = get_min_max(list(temp.geometry.values[0].exterior.coords))
            return bbox
        



