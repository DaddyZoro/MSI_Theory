import pandas as pd

file_name = 'eValB1.txt'

df = pd.read_fwf('eValB1.txt')
df.to_csv('eValB1.csv')