import pandas as pd
import numpy as np 

files = ['E:\Python\Python_Projects\Projects\Excel_Automation\SampleData.xlsx', 'E:\Python\Python_Projects\Projects\Excel_Automation\SampleData2.xlsx']

for file in files:
    df = pd.read_excel(file)
    # Now I want to check information
    # about pencil item
    pencil = df['Rep'].where(df['Item'] == 'Pencil')
    print(file)
    print(pencil)