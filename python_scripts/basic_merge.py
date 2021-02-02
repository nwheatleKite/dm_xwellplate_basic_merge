import pandas as pd
from .csv_string_to_df import csv_string_get_comments
from .csv_string_to_df import csv_string_to_df

def raw_data_list_to_df(raw_data_list):
    rawdatadf_list = []
    for raw_data in raw_data_list:
        raw_data_string = raw_data['data']
        raw_data_df = csv_string_to_df(raw_data_string)
        for key, value in raw_data.items():
            if key != "data":
                raw_data_df[key] = value
        rawdatadf_list.append(raw_data_df)
    combined_raw_data = pd.concat(rawdatadf_list, ignore_index=True)
    return combined_raw_data

def basic_merge(xwellplate_string, rawdata_list):
    # attempts to merge
    try:
        xwellplate_df = csv_string_to_df(xwellplate_string)
        rawdata_df = raw_data_list_to_df(rawdata_list)
        success = False
        messages= []
        
        if 'well_id_0' in rawdata_df.columns:
            data = xwellplate_df.merge(rawdata_df, left_on=["plate_id", "well_id_0"], right_on=["plate_id", "well_id_0"], how="left", suffixes=['_xwp', '_rd' ])
            data = data.to_csv(index=False)
            success = True
        elif 'well_id' in rawdata_df.columns:
            data = xwellplate_df.merge(rawdata_df, left_on=["plate_id", "well_id"], right_on=["plate_id", "well_id"], how="left", suffixes=['_xwp', '_rd' ])
            data = data.to_csv(index=False)
            success = True
        else:
            data = ""
            messages.append("rawdata column names must conatin either 'well_id_0' or 'well_id'.")
            if not 'plate_id' in rawdata_df.columns:
                messages.append("rawdata column names must contain 'plate_id'.")
        return {'success':success, 'data':data, "messages":messages}
    except Exception as e:
        return {'success': False, 'data':"", "messages": ["basic_merge() python function raised ERROR : ", str(e)]}



