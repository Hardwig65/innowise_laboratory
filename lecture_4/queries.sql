--- #1 Creating tables
CREATE TABLE students
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name  TEXT NOT NULL,
    birth_year INTEGER
);

CREATE TABLE grades
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject    TEXT    NOT NULL,
    grade      INTEGER CHECK (grade BETWEEN 1 AND 100),
    FOREIGN KEY (student_id) REFERENCES students (id)
);

--- #2 Inserting info in tables
INSERT INTO students (full_name, birth_year)
VALUES ('Alice Johnson', 2005),
       ('Brian Smith', 2004),
       ('Carla Reyes', 2006),
       ('Daniel Kim', 2005),
       ('Eva Thompson', 2003),
       ('Felix Nguyen', 2007),
       ('Grace Patel', 2005),
       ('Henry Lopez', 2004),
       ('Isabella Martinez', 2006);

INSERT INTO grades (student_id, subject, grade)
VALUES (1, 'Math', 88),
       (1, 'English', 92),
       (1, 'Science', 85),

       (2, 'Math', 75),
       (2, 'History', 83),
       (2, 'English', 79),

       (3, 'Science', 95),
       (3, 'Math', 91),
       (3, 'Art', 89),

       (4, 'Math', 84),
       (4, 'Science', 88),
       (4, 'Physical Education', 93),

       (5, 'English', 90),
       (5, 'History', 85),
       (5, 'Math', 88),

       (6, 'Science', 72),
       (6, 'Math', 78),
       (6, 'English', 81),

       (7, 'Art', 94),
       (7, 'Science', 87),
       (7, 'Math', 90),

       (8, 'History', 77),
       (8, 'Math', 83),
       (8, 'Science', 80),

       (9, 'English', 96),
       (9, 'Math', 89),
       (9, 'Art', 92);


--- #3 finding all grades for Alice
select full_name, grades.subject, grades.grade
from students
         join grades on students.id = grades.student_id
where full_name = 'Alice Johnson'

--- #4 Calculating average grades for students
select full_name, avg(grades.grade) as average
from students
         join grades on students.id = grades.student_id
group by students.id, full_name

--- #5 Find all students borned after 2004
SELECT id, full_name, birth_year
FROM students
WHERE birth_year > 2004

--- #6 Lists all subjects and their avg grades
SELECT subject, AVG(grade) AS average_grade
FROM grades
GROUP BY subject

--- #7 Top 3 students and their AVG grades
SELECT full_name, AVG(grades.grade) AS average_grade
FROM students
         JOIN grades ON students.id = grades.student_id
GROUP BY full_name
ORDER BY average_grade DESC LIMIT 3

--- #8 lists all students who have scored below 80
SELECT DISTINCT full_name, grades.subject, grades.grade
FROM students
         JOIN grades ON students.id = grades.student_id
WHERE grades.grade < 80
ORDER BY full_name



