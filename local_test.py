from python_scripts.basic_merge import basic_merge
from python_scripts.csv_string_to_df import csv_string_to_df

import pandas as pd
xwellplate_file = '/Users/nicolewheatley/Dev/basic_merge/example_files/20201105_xwellplate_Cell_Count_IQue_1X96WellPlates.csv'
rawdata_file = '/Users/nicolewheatley/Dev/basic_merge/example_files/20201022_RawData_Cell_Count_IQue.csv'


with open(xwellplate_file, 'r') as file:
    xwellplate_text = file.read()
    print(xwellplate_text)
    input()

with open(rawdata_file, 'r') as file:
    rawdata_text = file.read()
    print(rawdata_text)
    input()

rawdata_list = [{"data":rawdata_text}]
output = basic_merge(xwellplate_text, rawdata_list)

print(output)

data = output['data']

data_df = csv_string_to_df(data)

print(data_df)
