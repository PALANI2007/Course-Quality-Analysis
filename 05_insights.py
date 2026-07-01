import pandas as pd

df=pd.read_excel(r"C:\Users\Lenovo\Downloads\Master_Education_Cleaned.xlsx")

print("="*60)
print("PROJECT INSIGHTS")
print("="*60)

print()

print("Total Courses :",len(df))

print("Average Rating :",round(df["Student_Rating"].mean(),2))

print("Average Completion :",round(df["Completion_Rate"].mean(),2))

print("Highest Rated Course")

print(df.loc[df["Student_Rating"].idxmax()])

print()

print("Lowest Rated Course")

print(df.loc[df["Student_Rating"].idxmin()])

print()

print("Best Department")

print(df.groupby("Department")["Student_Rating"].mean().sort_values(ascending=False).head(1))

print()

print("Best Author")

print(df.groupby("Author")["Student_Rating"].mean().sort_values(ascending=False).head(1))