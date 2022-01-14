# Version: 	1.0.0
# Author: 	Gregory Giuliani
# Python script to optimize raster files before publication in GeoServer

import sys, os, string

inputFld = "/Users/Greg/Desktop/ndvi/"
outputFld = "/Users/Greg/Desktop/new2/"
gdalPath = "/Library/Frameworks/GDAL.framework/Versions/Current/Programs/"

# Recompress all GeoTIFFs using DEFLATE compression method
listing = os.listdir(inputFld) # list files
for infile in listing:
	os.system(gdalPath+'gdal_translate -co "COMPRESS=DEFLATE" -co "TILED=YES" --config GDAL_NUM_THREADS 4 -co "BLOCKXSIZE=512" -co "BLOCKYSIZE=512" --config GDAL_CACHEMAX 512 '+inputFld+infile+' '+outputFld+infile) 

# Add Internal Overviews to GeoTIFFs
listing2 = os.listdir(outputFld) # list files
for infile2 in listing2:
    os.system(gdalPath+'gdaladdo --config COMPRESS_OVERVIEW DEFLATE --config GDAL_NUM_THREADS 4 --config GDAL_TIFF_OVR_BLOCKSIZE 512 --config GDAL_CACHEMAX 512 '+outputFld+infile2+' 2 4 8 16 32 64')