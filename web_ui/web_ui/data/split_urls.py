import os
import json

with open('urls.json') as jsf:
    data = json.load(jsf)

#chunk data
n = 100
ch = [ data[i*n:(i+1)*n] for i in range( (len(data)+n-1) // n ) ]

#for each chunk create a folder and dumps 100 urls
for i in range(len(ch)):
     os.mkdir(f'./batches/b_{i}')
     with open(f'./batches/b_{i}/url.json','w') as o:
            json.dump(ch[i],o)