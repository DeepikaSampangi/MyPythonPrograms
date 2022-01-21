import os

curr_dir = os.path.dirname(__file__)
file_path = os.path.join(curr_dir, "weather_data.csv")
# with open(file_path) as file:
#     content = file.readlines()
#     print(content)

import csv

with open(file_path) as file:
    data = csv.reader(file)
    print(data)
