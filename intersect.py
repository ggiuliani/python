#export PATH=/Library/Frameworks/GDAL.framework/Programs:$PATH
#ogr2ogr -clipsrc polygonforclipping.shp out.shp in.shp
#ogr2ogr -clipsrc Desktop/output/kba_ch.shp Desktop/output/out.shp Desktop/output/wdpa_ch.shp

import sys, os, string
poly_for_clip = "/Users/greg/Desktop/output/kba_ch.shp"
poly_in = "/Users/greg/Desktop/output/wdpa_ch.shp"
poly_out = "/Users/greg/Desktop/output/out.shp"
ogrPath = "/Library/Frameworks/GDAL.framework/Programs/"

os.system(ogrPath+'ogr2ogr -clipsrc '+poly_for_clip+' '+poly_out+' '+poly_in)