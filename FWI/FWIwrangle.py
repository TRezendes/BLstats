import pandas as pd
import json
import csv

Fnames = ['area','case','category2','datatype','event','industry','occupation','source']
buildDict={}

for name in Fnames:
    filename = 'C:\\Users\\trezendes\\projects\\BLStats\\FWI\\codes\\fw.' + name + '.tsv'
    with open(filename) as tsv_file:
        df = pd.read_csv(tsv_file,delimiter='\t')
        buildDict[name] = df

with open('C:\\Users\\trezendes\\projects\\BLStats\\FWI\\detailedFWI.json') as JSONfile:
    fwiDF = pd.read_json(JSONfile)

ind1 = [3,6,]






fwiDF['seriesID'][0][:4]

'''

                         1         2
		12345678901234567890
Series ID   	FWU00X00000080M70

Positions       Value           Field Name
1-2             FW              Prefix
3               U               Seasonal Adjustment Code
4-6             00X             Category Code
7-12            000000          Detail Code (Industry, Event or Exposure, Primary Source, Secondary Source, Occupation)
13              8               Data Type Code
14              0               Case Type Code
15-17           M70             Area Code
'''
