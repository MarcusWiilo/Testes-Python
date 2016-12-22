import pandas as pd
from IPython.display import display

import csv
data = pd.read_csv("ch02-data.csv")

print "well"
display(data.head(10))
