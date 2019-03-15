# script for running in pyQGIS - SDESMET

#import processing tool box in QGIS
import processing
#import os library
import os
# get user to provide folder path to directory containing results shape files. one directory, must not contain anything other than target files

#create a user input box and ask for a string
from PyQt4.QtGui import *
qid = QInputDialog()
title = "Enter path to shapefiles"
label = "inputfile path"
mode = QLineEdit.Normal
default = "<path?>"
text, ok = QInputDialog.getText(qid, title, label, mode, default)

# convert user input into a string
shapepath = str(text)

# get a list of files in user input directory
filelist = os.listdir(shapepath)

#filter down list to just the shapefiles
print filelist
for x in filelist:
	if ".shp" in x:
		shplist.append(x)
		
print shplist

# ask user for path to save results to.
qid2 = QInputDialog()
title2 = "Enter path to save rasters"
label2 = "outfile path"
mode2 = QLineEdit.Normal
default2 = "<path?>"
text2, ok = QInputDialog.getText(qid2, title2, label2, mode2, default2)	


outfldr = str(text2)

#loop through files in list running the gdal rasterize function

for shapefile in shplist
	outputpath = outfldr+'\\'+shapefile
	processing.runalg("gdalogr:rasterize",shapefile,"2D_depth",0,8478,434147,outputpath)

