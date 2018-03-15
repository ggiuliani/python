import sys, os, string
shp_in = "/Users/greg/Desktop/output/kba_ch.shp"
csv_out = "/Users/greg/Desktop/output/out.csv"
ogrPath = "/Library/Frameworks/GDAL.framework/Programs/"

os.system(ogrPath+'ogr2ogr -f "CSV" '+csv_out+' '+shp_in)