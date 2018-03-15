# Version: 	1.0.0
# Author: 	Gregory Giuliani
#			University of Geneva 
#			Institute for Environmental Sciences/enviroSPACE
#			Uni Carl-Vogt
#			66 boulevard Carl-Vogt
#			CH - 1205 Genève
#			http://www.unige.ch/envirospace/people/giuliani/
#			http://www.unige.ch/envirospace
#
# Python script to convert KML to Shapefile
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import sys, os, string

inputFld = "/Users/Greg/Desktop/kml/"
outputFld = "/Users/Greg/Desktop/shp/"
ogrPath = "/Library/Frameworks/GDAL.framework/Versions/1.8/Programs/"

listing = os.listdir(inputFld)
for infile in listing:
	os.system(ogrPath+'ogr2ogr -f "ESRI Shapefile" '+outputFld+' '+inputFld+infile) 