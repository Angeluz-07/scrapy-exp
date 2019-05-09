
import json
import pandas as pd

#getting my data from json file
#this data contains features about a set of houses on sale from olx webpage in ecuador
file_path = '../scraped_data/olx_houses_ec.json'
with open(file_path) as f:
	data = json.load(f)


#use pandas library to cook a matrix with samples to feed ML training
hs = pd.DataFrame(data = data, columns = ['surface','bathrooms','bedrooms','price'])

#first let's fix the points in some prices(e.g. '1.000.000') because they can't be converted
#to floats, and it seems that is causing troubles on plotting

#https://python-forum.io/Thread-pandas-dataframe-replace-regex
hs.price.replace('\.','',regex = True, inplace= True)

hs.dropna(inplace = True)

#for purposes of my learning I will cutt off samples based on my sense of prices and surfaces

hs_ol=hs.astype(float)
#keep houses with prices [2000,15000] & surfaces below 200 m2
index_hs_outliers = hs_ol[ (hs_ol['price'] > 100000) | 
                           (hs_ol['price'] < 15000)  | 
                           (hs_ol['surface'] < 200)  | 
                           (hs_ol['surface'] > 800)   ].index

hs_no_outliers=hs.drop(index_hs_outliers)
hs_no_outliers.info()
print(hs_no_outliers.tail())

output_file_path= '../scraped_data/olx_houses_ec_cleaned.csv'
hs_no_outliers.to_csv(output_file_path, index = False)
#I had to lose about 600 sample from this dataset to get a ready training set
