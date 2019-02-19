import pandas as pd

fname_ = input("csv filename? ")
dtime_ = input("Column name of the date time object? ")
y_ = input("Column name of the y object? ")
output_ = input("desired output file name? ")

df = pd.read_csv(fname_)
df = df[[dtime_, y_]]
df['ds'] = df[dtime_]
df['y'] = df[y_]
df = df[['ds','y']]

df.to_csv(output_, index=False)


