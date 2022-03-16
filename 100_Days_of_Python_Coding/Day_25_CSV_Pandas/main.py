import os

import pandas as pd

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

data = pd.read_csv(file_path)
print(data["temp"])
temp_list = data["temp"].to_list()
print(f"Avg temp : {sum(temp_list)/len(temp_list)}")

print(f'Avg : {data["temp"].mean()}')

print(f"Max temp : {max(temp_list)}")
print(f'Max temp : {data["temp"].max()}')

# Get Data in a Row
print(data[data["day"] == "Monday"])

# Max Temp row
print(f'{data[data["temp"] == data["temp"].max()]}')

# Monday's temp in Fahrenheit

monday = data[data["day"] == "Monday"]
fahren_temp = (int(monday.temp) * (9 / 5)) + 32
print(f"Monday temp in fahrenheit {fahren_temp}")


# Create Dataframe from Scratch

data_dict = {"students": ["Amy", "Jack", "Thea"], "scores": [76, 56, 65]}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
