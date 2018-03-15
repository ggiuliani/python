#script to intersect two shapefiles
#author: Gregory Giuliani (University of Geneva)
#version: 1.0.0

import sys, os, string
poly_for_clip = "/Users/greg/Desktop/output/kba_ch.shp"
poly_in = "/Users/greg/Desktop/output/wdpa_ch.shp"
poly_out = "/Users/greg/Desktop/output/out.shp"
ogrPath = "/Library/Frameworks/GDAL.framework/Programs/"

os.system(ogrPath+'ogr2ogr -clipsrc '+poly_for_clip+' '+poly_out+' '+poly_in)