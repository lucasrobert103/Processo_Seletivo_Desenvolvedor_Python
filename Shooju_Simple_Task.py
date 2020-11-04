from urllib import request
from zipfile import ZipFile
from io import BytesIO
import csv
from operator import itemgetter
import itertools as it
import json
import os

def make_points_quality(group):
    '''
        This function return a list of points and quality
        over the months and years
        :argument one group of filters groups
    '''
    points = []
    quality = []
    for row in group:
        points.append([row['TIME_PERIOD'] + ' , ' + row['OBS_VALUE']])
        quality.append([row['TIME_PERIOD'] + ' , ' + row['ASSESSMENT_CODE']])

    return points, quality

#As mentioned, place the order and save a CSV in the data mass
response = request.urlopen("https://www.jodidata.org/_resources/files/downloads/gas-data/jodi_gas_csv_beta.zip")
if  os.path.exists("data") != True:
    os.mkdir("data")

unzip = ZipFile(BytesIO(response.read()))
unzip.extractall("data")
unzip.close()

#Open the CSV file to read the files
with open("data/jodi_gas_beta.csv", 'r') as mycsv:
    #Read data
    reader = csv.DictReader(mycsv)
    #Sort the data according to your primary keys
    primary_key = itemgetter('REF_AREA', 'ENERGY_PRODUCT', 'FLOW_BREAKDOWN', 'UNIT_MEASURE',
                             'TIME_PERIOD')
    reader = sorted(reader, key=primary_key)

# Limit to first 200 rows for TESTING.
# reader = [row for row in it.islice(reader, 200)]

# Group the data by designated keys
keys, groups = [], []
keyfunc = itemgetter('REF_AREA', 'ENERGY_PRODUCT', 'FLOW_BREAKDOWN', 'UNIT_MEASURE')
for k, g in it.groupby(reader, key=keyfunc):
    keys.append(k[0]+k[1]+k[2]+k[3])
    groups.append(list(g))

#Creating a JSON data
for i, group in enumerate(groups):
    #Calling the function make_points_quality for do the lists of points and quality
    points, quality = make_points_quality(group)
    result = {
                'series_id': ''.join(keys[i]),
                'points': points,
                'series': {
                    'country': ''.join(group[0]['REF_AREA']),
                    'product': ''.join(group[0]['ENERGY_PRODUCT']),
                    'flow': ''.join(group[0]['FLOW_BREAKDOWN']),
                    'unit_meassure': ''.join(group[0]['UNIT_MEASURE']),
                    'quality': quality
                }
              }
    # Transforming the data in Json
    result = json.dumps(result)
    # Printing one Json object per line
    print(result)

    #Obrigado por essa oportunidade