import pandas as pd

df=pd.read_excel(r"C:\Users\Lenovo\Downloads\Master_Education_Cleaned.xlsx")

print("="*60)
print("STATISTICS")
print("="*60)

print(df.describe())

print("\n")

print("Missing Values")
print(df.isnull().sum())

print("\n")

print("Duplicate Rows")
print(df.duplicated().sum())

print("\n")

print("Average Rating")
print(df["Student_Rating"].mean())

print("\nHighest Rating")
print(df["Student_Rating"].max())

print("\nLowest Rating")
print(df["Student_Rating"].min())

print("\nAverage Grammar")
print(df["Grammar_Score"].mean())

print("\nAverage Readability")
print(df["Readability_Score"].mean())

print("\nAverage Completion")
print(df["Completion_Rate"].mean())