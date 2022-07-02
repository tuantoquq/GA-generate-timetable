## Timetable Generator

### Constraint
    
    1. No teacher can hold two classes at the same time (same lesson)
    2. No classroom can receive two classes at the same time (same lesson)
    3. Each teacher can only teach one subject

### Constants

    1. Number lesson per day: 12 (LESSON1, LESSON2, ..., LESSON12)
    2. Number of classroom is NUM_ROOM: (ROOM1, ROOM2, ...)    
    3. Number of learning day is 6 days per week.
    4. Number of teacher is NUM_TEACHER: (TEACHER1, TEACHER2, ...)
    5. Number of subject is 11 : 
        Math, Physic, Chemistry, Literature, History, Geography, Biology, 
        Civic Education (GDCD), Physical Education, English, Technology (Công nghệ), 
        Information Technology (Tin học), National Defense and Security (QPAN)
    6. Quota of lesson for each teacher per week: most 17 lessons/week
    8. Number of classes is NUM_CLASSES: (CLASS1, CLASS2, ...)
    