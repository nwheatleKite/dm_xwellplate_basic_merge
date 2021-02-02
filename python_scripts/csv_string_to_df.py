
import pandas as pd
from io import StringIO
import re


def csv_string_to_df(csv_string):
    # takes a string csv, and transforms into pandas dataframe
    if csv_string == None or csv_string == "":
        return None
    else:
        df = pd.read_csv(StringIO(csv_string),
                        comment="#",
                        na_values=["", "Static-NA", "NA"],
                        true_values=["True", "TRUE", "true"],
                        false_values=["False", "FALSE", "false"],
                        )
        first_col = df.columns[0]
        if re.findall('ï»¿', first_col):
            # sometimes there is a BOM mark from opening/resaving file before upload
            new_first = first_col.replace('ï»¿', '')
            df[new_first] = df[first_col]
            df.drop(columns=[first_col], inplace=True)
        return df


def csv_string_get_comments(csv_string, comment="#"):
    if csv_string == None or csv_string == "":
        return []
    else:
      csv_list = csv_string.splitlines()
      comment_list = []
      for line in csv_list:
          if re.match("^#", line):
              comment_list.append(line)
    return comment_list
