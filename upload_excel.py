import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# PostgreSQL Details
username = "postgres"
password = quote_plus("Pala@2007")   # @ symbol safe
host = "localhost"
port = "5432"
database = "course_quality_db"

# Connection
engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

# Excel File
file_path = r"C:\Users\Lenovo\Downloads\Master_Education_Cleaned.xlsx"

# Read Excel
df = pd.read_excel(file_path)

# Rename Columns
df.columns = [
    "course_id",
    "course_name",
    "department",
    "module",
    "lesson_title",
    "content_word_count",
    "sentence_count",
    "readability_score",
    "grammar_score",
    "learning_objective_match",
    "student_rating",
    "completion_rate",
    "feedback_count",
    "reading_time_minutes",
    "publish_date",
    "author",
    "difficulty_level",
    "overall_quality"
]

# Upload to PostgreSQL
df.to_sql(
    "course_content",
    engine,
    if_exists="replace",
    index=False
)

print("✅ Excel Uploaded Successfully!")