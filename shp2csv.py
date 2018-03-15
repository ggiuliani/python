#script to extract some selected attribute from a shapefile and export them in a CSV file
#author: Gregory Giuliani (University of Geneva)
#version: 1.0.0

import sys, os, string
shp_in = "/Users/greg/Desktop/output/kba_ch.shp"
csv_out = "/Users/greg/Desktop/output/out.csv"
ogrPath = "/Library/Frameworks/GDAL.framework/Programs/"

os.system(ogrPath+'ogr2ogr -f "CSV" -select "SitRecID,area" '+csv_out+' '+shp_in)