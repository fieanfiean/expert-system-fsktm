# data/students.py
# Mock student database for testing the expert system

STUDENTS = {
    "S001": {
        "name": "Ahmad Faiz",
        "cgpa": 3.45,
        "semester": 4,
        "programme": "AI",
        "completed_courses": ["WIX1001", "WIX1002", "WIX1003", "WIA1002", "WIA1005", "WIA1003"],
        "interest": "AI / Machine Learning",
        "is_fyp_semester": False,
        "remaining_credits": 78
    },
    "S002": {
        "name": "Siti Nurhaliza",
        "cgpa": 2.85,
        "semester": 5,
        "programme": "AI",
        "completed_courses": ["WIX1001", "WIX1002", "WIX1003", "WIA1002", "WIA1005", "WIA1003", "WIA1006", "WIA1007", "WIA2001"],
        "interest": "Data Science",
        "is_fyp_semester": False,
        "remaining_credits": 45
    },
    "S003": {
        "name": "Tan Wei Ming",
        "cgpa": 1.95,
        "semester": 3,
        "programme": "AI",
        "completed_courses": ["WIX1001", "WIX1002"],
        "interest": "AI / Machine Learning",
        "is_fyp_semester": False,
        "remaining_credits": 95
    },
    "S004": {
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
        "is_fyp_semester": True,  # FYP semester - will trigger Heuristic 1
        "remaining_credits": 28
    },
    "S005": {
        "name": "Muhammad Idris",
        "cgpa": 3.15,
        "semester": 4,
        "programme": "AI",
        "completed_courses": ["WIX1001", "WIX1002", "WIX1003", "WIA1002", "WIA1005"],
        "interest": "Networking",
        "is_fyp_semester": False,
        "remaining_credits": 82
    },
    "S006": {
        "name": "Lim Xin Yi",
        "cgpa": 2.35,
        "semester": 5,
        "programme": "AI",
        "completed_courses": ["WIX1001", "WIX1002", "WIX1003", "WIA1002", "WIA1005", "WIA1003", "WIA1006"],
        "interest": "AI / Machine Learning",
        "is_fyp_semester": False,
        "remaining_credits": 55
    },
    "S007": {
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
    "S008": {
        "name": "Nurul Izzati",
        "cgpa": 3.05,
        "semester": 3,
        "programme": "AI",
        "completed_courses": ["WIX1001", "WIX1002", "WIX1003", "WIA1002"],
        "interest": "Software Development",
        "is_fyp_semester": False,
        "remaining_credits": 88
    }
}

def get_student(student_id):
    """Retrieve student by ID"""
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

if __name__ == "__main__":
    print("=== Mock Student Database ===")
    for student in get_student_summary():
        print(f"{student['id']}: {student['name']} (CGPA: {student['cgpa']}, Semester: {student['semester']})")