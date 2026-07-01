import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel(r"C:\Users\Lenovo\Downloads\Master_Education_Cleaned.xlsx")

numeric=df.select_dtypes(include="number")

corr=numeric.corr()

print(corr)

plt.figure(figsize=(10,8))
plt.imshow(corr)
plt.colorbar()

plt.xticks(range(len(corr.columns)),corr.columns,rotation=90)
plt.yticks(range(len(corr.columns)),corr.columns)

plt.title("Correlation Matrix")

plt.show()