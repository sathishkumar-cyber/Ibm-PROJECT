import pandas as pd
a=pd.read_csv("./data/shops_en.csv")#load the dataset

a.dropna(inplace=True)
a.drop_duplicates(inplace=True)

a['shop_id']=pd.to_numeric(a['shop_id'])

print(a)