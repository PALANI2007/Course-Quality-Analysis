import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel(r"C:\Users\Lenovo\Downloads\Master_Education_Cleaned.xlsx")

# -------------------
# Rating Distribution
# -------------------

plt.figure(figsize=(8,5))
plt.hist(df["Student_Rating"],bins=10)
plt.title("Student Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.savefig("graphs/rating_distribution.png")
plt.show()

# -------------------
# Department
# -------------------

plt.figure(figsize=(8,5))
df["Department"].value_counts().plot(kind="bar")
plt.title("Department Wise Courses")
plt.savefig("graphs/department.png")
plt.show()

# -------------------
# Overall Quality
# -------------------

plt.figure(figsize=(7,7))
df["Overall_Quality"].value_counts().plot(kind="pie",autopct="%1.1f%%")
plt.title("Overall Quality")
plt.ylabel("")
plt.savefig("graphs/quality.png")
plt.show()

# -------------------
# Difficulty
# -------------------

plt.figure(figsize=(8,5))
df["Difficulty_Level"].value_counts().plot(kind="bar")
plt.title("Difficulty")
plt.savefig("graphs/difficulty.png")
plt.show()

# -------------------
# Completion Rate
# -------------------

plt.figure(figsize=(8,5))
plt.hist(df["Completion_Rate"])
plt.title("Completion Rate")
plt.savefig("graphs/completion.png")
plt.show()

# -------------------
# Feedback Count
# -------------------

plt.figure(figsize=(8,5))
plt.hist(df["Feedback_Count"])
plt.title("Feedback Count")
plt.savefig("graphs/feedback.png")
plt.show()

# -------------------
# Reading Time
# -------------------

plt.figure(figsize=(8,5))
plt.hist(df["Reading_Time_Minutes"])
plt.title("Reading Time")
plt.savefig("graphs/reading_time.png")
plt.show()

# -------------------
# Top Courses
# -------------------

top=df.sort_values("Student_Rating",ascending=False)

plt.figure(figsize=(12,5))
plt.bar(top["Course_Name"].head(10),top["Student_Rating"].head(10))
plt.xticks(rotation=90)
plt.title("Top Rated Courses")
plt.savefig("graphs/top_courses.png")
plt.show()

# -------------------
# Bottom Courses
# -------------------

low=df.sort_values("Student_Rating")

plt.figure(figsize=(12,5))
plt.bar(low["Course_Name"].head(10),low["Student_Rating"].head(10))
plt.xticks(rotation=90)
plt.title("Lowest Rated Courses")
plt.savefig("graphs/low_courses.png")
plt.show()

# -------------------
# Scatter Plot
# -------------------

plt.figure(figsize=(8,5))
plt.scatter(df["Readability_Score"],df["Student_Rating"])
plt.xlabel("Readability")
plt.ylabel("Rating")
plt.title("Readability vs Rating")
plt.savefig("graphs/readability_vs_rating.png")
plt.show()