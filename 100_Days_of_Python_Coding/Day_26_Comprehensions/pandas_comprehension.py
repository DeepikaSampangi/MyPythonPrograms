import pandas as pd

std_dict = {
    "name":["Klaus", "Elijha", "Hayley"],
    "score":[100,80,90]
}

std_df = pd.DataFrame(std_dict)
print(std_df)

for (index, row) in std_df.iterrows():
    print(row)