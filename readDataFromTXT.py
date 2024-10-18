import pandas as pd
import re

file_folder = "UIUC-propDB/volume-3/data/"
file_name ="ancf_12x13_0784od_4015.txt"
file_path = file_folder+file_name


def readData(file_path,file_name):
    spec = file_name.split("_")
    RPM = re.findall(r'\d+',spec[-1])[0]

    d = float(spec[1].split("x")[0])
    d = d/10 if d>100 else d

    pitch = float(spec[1].split("x")[1])
    pitch = pitch / 10 if pitch > 13 else pitch

    df = pd.read_csv(file_path, delim_whitespace=True, header=0)
    float_df = df.astype(float)

    return float_df,RPM,d,pitch


if __name__ == "__main__":
    print(readData(file_path,file_name))
