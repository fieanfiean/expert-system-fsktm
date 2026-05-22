# data/students.py
# Mock student database for testing the expert system
# Using 8-digit UM matric number format

STUDENTS = {
    "24004601": {
        "name": "Ahmad Faiz",
        "cgpa": 3.45,
        "semester": 4,
        "programme": "AI",
        "completed_courses": ["WIX1001", "WIX1002", "WIX1003", "WIA1002", "WIA1005", "WIA1003"],
        "interest": "AI / Machine Learning",
        "is_fyp_semester": False,
        "remaining_credits": 78
    },
    "24004602": {
        "name": "Siti Nurhaliza",
        "cgpa": 2.85,
        "semester": 5,
        "programme": "AI",
        "completed_courses": ["WIX1001", "WIX1002", "WIX1003", "WIA1002", "WIA1005", "WIA1003", "WIA1006", "WIA1007", "WIA2001"],
        "interest": "Data Science",
        "is_fyp_semester": False,
        "remaining_credits": 45
    },
    "24004603": {
        "name": "Tan Wei Ming",
        "cgpa": 1.95,
        "semester": 3,
        "programme": "AI",
        "completed_courses": ["WIX1001", "WIX1002"],
        "interest": "AI / Machine Learning",
        "is_fyp_semester": False,
        "remaining_credits": 95
    },
    "24004604": {
        "name": "Priya Kaur",
        "cgpa": 3.78,
        "semester": 6,
        "programme": "AI",
        "completed_courses": [
            "WIX1001", "WIX1002", "WIX1003", "WIA1002", "WIA1005", "WIA1003",
            "WIA1006", "WIA1007", "WIA2001", "WIA2003", "WIA2004", "WIA2005",
            "WIA2006", "WIA2007"
        ],
        "interest": "AI / Machine Learning",
        "is_fyp_semester": True,
        "remaining_credits": 28
    },
    "24004605": {
        "name": "Muhammad Idris",
        "cgpa": 3.15,
        "semester": 4,
        "programme": "CSN",
        "completed_courses": ["WIX1001", "WIX1002", "WIX1003", "WIA1002", "WIA1005"],
        "interest": "Networking",
        "is_fyp_semester": False,
        "remaining_credits": 82
    },
    "24004606": {
        "name": "Lim Xin Yi",
        "cgpa": 2.35,
        "semester": 5,
        "programme": "SE",
        "completed_courses": ["WIX1001", "WIX1002", "WIX1003", "WIA1002", "WIA1005", "WIA1003", "WIA1006"],
        "interest": "Software Development",
        "is_fyp_semester": False,
        "remaining_credits": 55
    },
    "24004607": {
        "name": "Ravi Chandran",
        "cgpa": 3.92,
        "semester": 7,
        "programme": "AI",
        "completed_courses": [
            "WIX1001", "WIX1002", "WIX1003", "WIA1002", "WIA1005", "WIA1003",
            "WIA1006", "WIA1007", "WIA2001", "WIA2003", "WIA2004", "WIA2005",
            "WIA2006", "WIA2007", "WID2001", "WID2002"
        ],
        "interest": "AI / Machine Learning",
        "is_fyp_semester": True,
        "remaining_credits": 15
    },
    "24004608": {
        "name": "Nurul Izzati",
        "cgpa": 3.05,
        "semester": 3,
        "programme": "MM",
        "completed_courses": ["WIX1001", "WIX1002", "WIX1003", "WIA1002"],
        "interest": "Multimedia",
        "is_fyp_semester": False,
        "remaining_credits": 88
    }
}

def get_student(student_id):
    """Retrieve student by ID (8-digit matric number)"""
    return STUDENTS.get(student_id, None)

def get_all_students():
    """Return all student IDs for dropdown"""
    return list(STUDENTS.keys())

def get_student_summary():
    """Return summary of all students for testing"""
    summary = []
    for sid, data in STUDENTS.items():
        summary.append({
            "id": sid,
            "name": data["name"],
            "cgpa": data["cgpa"],
            "semester": data["semester"],
            "courses_completed": len(data["completed_courses"])
        })
    return summary

def student_exists(student_id):
    """Check if a student ID exists in the database"""
    return student_id in STUDENTS

def add_student(student_id, student_data):
    """Add a new student to the database (for future expansion)"""
    if student_id in STUDENTS:
        return False
    STUDENTS[student_id] = student_data
    return True

if __name__ == "__main__":
    print("=== Mock Student Database ===")
    print(f"Total students: {len(STUDENTS)}")
    print("\nStudent List:")
    for student in get_student_summary():
        print(f"  {student['id']}: {student['name']} (CGPA: {student['cgpa']}, Semester: {student['semester']}, Courses: {student['courses_completed']})")