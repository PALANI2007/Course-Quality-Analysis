-- Total Courses
SELECT COUNT(*) AS Total_Courses
FROM course_content;

-- Average Student Rating
SELECT AVG(student_rating) AS Average_Rating
FROM course_content;

-- Department Wise Average Rating
SELECT department,
AVG(student_rating) AS Avg_Rating
FROM course_content
GROUP BY department;

-- Highest Rated Course
SELECT course_name, student_rating
FROM course_content
ORDER BY student_rating DESC
LIMIT 10;

-- Completion Rate
SELECT AVG(completion_rate)
FROM course_content;

-- Overall Quality
SELECT AVG(overall_quality)
FROM course_content;

-- Performance Distribution
SELECT performance,
COUNT(*)
FROM course_content
GROUP BY performance;

-- Feedback Count
SELECT SUM(feedback_count)
FROM course_content;