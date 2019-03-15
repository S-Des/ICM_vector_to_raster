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

# ask user for raster dimensions or resolution
qidQ = QInputDialog()
titleQ = "type P to specify pixels per m2, or type W to specify pixel witdth and pixel height of raster"
labelQ = "type P or W"
modeQ = QLineEdit.Normal
defaultQ = "P or W?"
textQ, ok = QInputDialog.getText(qidQ, titleQ, labelQ, modeQ, defaultQ)	

# if the user has typed P, present another dialogue asking for the Pixels to m2 of map resolution
if textQ = 'P'
	qidP = QInputDialog()
	titleP = "How many pixels per map unit (i suggest 1 if you are not sure)"
	labelP = "pixels per map unit"
	modeP = QLineEdit.Normal
	defaultP = "pixels?"
	textP, ok = QInputDialog.getText(qidP, titleP, labelP, modeP, defaultP)	
	textW = '0' # set the width and height to 0 as we are using P instead
	textH = '0'

else 	
if textW = 'P'
	qidW = QInputDialog()
	titleW = "Raster width in pixels?"
	labelW = "width in pixels"
	modeW = QLineEdit.Normal
	defaultW = "width"
	textW, ok = QInputDialog.getText(qidW, titleW, labelW, modeW, defaultW)	
	
	qidH = QInputDialog()
	titleH = "Raster height in pixels"
	labelH = "height in pixels"
	modeH = QLineEdit.Normal
	defaultH = "height"
	textH, ok = QInputDialog.getText(qidH, titleH, labelH, modeH, defaultH)	
	textP = '0' # set the pixels per unit to 0 as we are using W&H instead

for shapefile in shplist
	outputpath = outfldr+'\\'+shapefile
	processing.runalg("gdalogr:rasterize",shapefile,"2D_depth",0,8478,434147,outputpath)

