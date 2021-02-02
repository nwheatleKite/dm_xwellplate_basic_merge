import pandas as pd
import sys
from io import StringIO

# checks if file is in proper csv format
# passes if pandas can read_csv, and if 2 or more columns, and if 2 or more rows, comments are OK

def validate_rawdata(text, required_column_names= []):
  try:
    messages = []
    success = True
    csv = pd.read_csv(StringIO(text), comment="#")
    cols = csv.columns
    index = csv.index
    if len(cols) < 2:
      messages.append('Must have 2 or more columns in csv')
      success = False
    if len(index) < 2:
      messages.append('Must have 2 or more rows in csv')
      success = False
      return {"success": success, "messages": messages}
    for req_col in required_column_names:
      if req_col not in cols:
        success = False
        messages.append(f'Required column {req_col} missing')
    if not ('well_id' in cols or 'well_id_0' in cols):
        messages.append(f'Requires either "well_id" or "well_id_0" column name in raw data to match xwell plate well ids.')
    return {"success": success, "messages": messages}
  except:
    return {"success": False, "messages": ["validate_csv(text) failed"]}
