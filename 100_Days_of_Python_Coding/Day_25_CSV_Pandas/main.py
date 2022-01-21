import os

curr_dir = os.path.dirname(__file__)
file_path = os.path.join(curr_dir, "weather_data.csv")
# with open(file_path) as file:
#     content = file.readlines()
#     print(content)

# import csv
#
# with open(file_path) as file:
#     data = csv.reader(file)
#     print(data)
#     temp = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#
#     print(temp)


import pandas as pd

data = pd.read_csv(file_path)
print(data["temp"])