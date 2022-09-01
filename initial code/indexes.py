# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 04:15:59 2022

@author: sarah
"""

import ee
import geemap

def index_NDVI(name, sat, mapLayer):
    """
    Calculate the NDVI (Normalized Difference Vegetation Index)
    @param name: path of the gee image - String 
           sat: Number of the Landsat used as source - number
    @return boolean False if the image is not coming from Ladsat 7 or 8
                    else, return True
    """
    image = ee.Image(name)
    if(sat == 7): 
        NIR = image.select('B4')
        Red = image.select('B3')
    elif(sat != 7 or sat != 8): 
        print("Error: Not a Landsat 7 or 8 image!")
        return False 
    elif(sat == 8): 
        NIR = image.select('B5')
        Red = image.select('B4')
    
    # Formula of NDVI = (NIR - Red)/(NIR + Red)
    ndvi = NIR.subtract(Red).divide(NIR.add(Red))

    palette = [
    'FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163', '99B718', '74A901',
    '66A000', '529400', '3E8601', '207401', '056201', '004C00', '023B01',
    '012E01', '011D01', '011301']

    mapLayer.addLayer(ndvi, {'palette': palette}, "NDVI")
    return True

def index_EVI(name, sat, mapLayer):
    """
    Calculate the EVI (Enhanced Vegetation Index)
    @param name: path of the gee image - String 
           sat: Number of the Landsat used as source - number
    @return boolean False if the image is not coming from Ladsat 7 or 8
                    else, return True
    """
    image = ee.Image(name)
    
    #Formula of EVI = 2.5 ((NIR - Red)/(NIR + 6*Red - 7.5*Blue + 1))
    if(sat == 7): 
        evi = image.expression('2.5 * ((NIR - RED) / (NIR + 6 * RED - 7.5 * BLUE + 1))', {
          'NIR': image.select('B4'),
          'RED': image.select('B3'),
          'BLUE': image.select('B1')})
    elif(sat == 8): 
        evi = image.expression('2.5 * ((NIR - RED) / (NIR + 6 * RED - 7.5 * BLUE + 1))', {
          'NIR': image.select('B5'),
          'RED': image.select('B4'),
          'BLUE': image.select('B2')})
    else: 
        print("Error: Not a Landsat 7 or 8 image!")
        return False
    
    mapLayer.addLayer(evi, {'min': -1, 'max': 1, 'palette': ['FF0000', '00FF00']}, 'EVI')
    return True

def index_NDWI(name, sat, mapLayer): 
    """
    Calculate the NDWI (Normalized Difference Water Index)
    @param name: path of the gee image - String 
           sat: Number of the Landsat used as source - number
    @return boolean False if the image is not coming from Ladsat 7 or 8
                    else, return True
    """
    image = ee.Image(name)
    if(sat == 7): 
        NIR = image.select('B4')
        SWIR = image.select('B5')
    elif(sat == 8): 
        NIR = image.select('B5')
        SWIR = image.select('B6')
    else: 
        print("Error : Not a Landsat 7 or 8 image!")
        return False
    #Formula of NDWI = (NIR - SWIR)/(NIR + SWIR)
    ndwi = NIR.subtract(SWIR).divide(NIR.add(SWIR))
    
    mapLayer.addLayer(ndwi, {'min': -1, 'max': 1, 'palette': ['FF0000', '00FF00']}, "NDWI")
    return True 

def index_MNDWI(name, sat, mapLayer): 
    """
    Calculate the MNDWI (Modified Normalized Difference Water Index)
    @param name: path of the gee image - String 
           sat: Number of the Landsat used as source - number
    @return boolean False if the image is not coming from Ladsat 7 or 8
                    else, return True
    """
    image = ee.Image(name)
    if(sat == 7): 
        Green = image.select('B2')
        SWIR = image.select('B5')
    elif(sat == 8): 
        Green = image.select('B3')
        SWIR = image.select('B6')
    else: 
        print("Error : Not a Landsat 7 or 8 image!")
        return False
    #Formula of MNDWI = (Green - SWIR)/(Green + SWIR)
    mndwi = Green.subtract(SWIR).divide(Green.add(SWIR))
    
    mapLayer.addLayer(mndwi, {'min': -1, 'max': 1, 'palette': ['FF0000', '00FF00']}, "MNDWI")
    return True 

def index_NDBI(name, sat, mapLayer): 
    """
    Calculate the NDBI (Normalized Difference Built-up Index)
    @param name: path of the gee image - String 
           sat: Number of the Landsat used as source - number
    @return boolean False if the image is not coming from Ladsat 7 or 8
                    else, return True
    """
    image = ee.Image(name)
    if(sat == 7): 
        NIR = image.select('B4')
        SWIR = image.select('B5')
    elif(sat == 8): 
        NIR = image.select('B5')
        SWIR = image.select('B6')
    else: 
        print("Error : Not a Landsat 7 or 8 image!")
        return False
    
    #Formula of NDBI = (SWIR - NIR)/(SWIR + NIR)
    ndbi = SWIR.subtract(NIR).divide(SWIR.add(NIR))
    
    mapLayer.addLayer(ndbi, {'min': -1, 'max': 1, 'palette': ['FF0000', '00FF00']}, "NDBI")
    return True

def index_SAVI(name, sat, mapLayer):
    """
    Calculate the SAVI (Soil Adjustment Vegetation Index)
    @param name: path of the gee image - String 
           sat: Number of the Landsat used as source - number
    @return boolean False if the image is not coming from Ladsat 7 or 8
                    else, return True    
    """
    image = ee.Image(name);
    if(sat == 7): 
        savi = image.expression('((NIR - Red)/(NIR + Red + 0.5))*1.5', {
          'NIR': image.select('B4'),
          'Red': image.select('B3')})
    elif(sat == 8): 
        savi = image.expression('((NIR - Red)/(NIR + Red + 0.5))*1.5', {
          'NIR': image.select('B5'),
          'Red': image.select('B4')})
    else: 
        print("Error : Not a Landsat 7 or 8 image!")
        return False
    mapLayer.addLayer(savi, {'min': -1, 'max': 1, 'palette': ['FF0000', '00FF00']}, "SAVI")
    return True

