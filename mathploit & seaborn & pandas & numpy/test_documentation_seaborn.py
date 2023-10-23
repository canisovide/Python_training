import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

data_sheets = pd.read_csv("../datasets/melb_data.csv/melb_data.csv")

# for column in data.columns:
#     print("{} type {}".format(column, data[column].dtype))
print(data_sheets['Date'].dtype)
data_sheets_1 = data_sheets.copy()
data_sheets_1['Date_parsed'] = pd.to_datetime(data_sheets_1.Date, format="mixed")
print(data_sheets_1.Date_parsed)


