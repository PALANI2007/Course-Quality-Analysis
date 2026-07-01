import pandas as pd

# Read Dataset
df = pd.read_excel(r"C:\Users\Lenovo\Downloads\Master_Education_Cleaned.xlsx")

print("="*60)
print("FIRST 5 RECORDS")
print("="*60)
print(df.head())

print("\n")

print("="*60)
print("LAST 5 RECORDS")
print("="*60)
print(df.tail())

print("\nShape :",df.shape)

print("\nColumns")
print(df.columns)

print("\nInfo")
print(df.info())