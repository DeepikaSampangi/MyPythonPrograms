import pandas as pd

full_sq_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_len = len(full_sq_data[full_sq_data["Primary Fur Color"] == "Gray"])
red_len = len(full_sq_data[full_sq_data["Primary Fur Color"] == "Cinnamon"])
black_len = len(full_sq_data[full_sq_data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_len, red_len, black_len],
}

print(data_dict)

len_df = pd.DataFrame(data_dict)
len_df.to_csv("squirrle_count.csv")
