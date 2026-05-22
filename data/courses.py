# data/courses.py - Complete Version for All 6 Programmes
# Based on UGHB2024_c.pdf - Faculty of Computer Science & Information Technology

# ==================== FACULTY CORE COURSES (All students must take) ====================
# Source: Handbook pages 53-54

FACULTY_CORE = {
    "WIX1001": {
        "name": "Computing Mathematics I",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": True,
        "semester": 1,
        "category": "Faculty Core"
    },
    "WIX1002": {
        "name": "Fundamentals of Programming",
        "credits": 5,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 1,
        "category": "Faculty Core"
    },
    "WIX1003": {
        "name": "Computer Systems and Organization",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 1,
        "category": "Faculty Core"
    },
    "WIX2001": {
        "name": "Thinking and Communication Skills",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "Faculty Core"
    },
    "WIX2002": {
        "name": "Project Management",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "Faculty Core"
    }
}

# ==================== PROGRAMME CORE - ARTIFICIAL INTELLIGENCE ====================
# Source: Handbook page 27

AI_CORE = {
    "WIA1002": {
        "name": "Data Structure",
        "credits": 5,
        "prerequisites": ["WIX1002"],
        "math_heavy": False,
        "semester": 2,
        "category": "AI Core"
    },
    "WIA1003": {
        "name": "Computer System Architecture",
        "credits": 3,
        "prerequisites": ["WIX1003"],
        "math_heavy": False,
        "semester": 2,
        "category": "AI Core"
    },
    "WIA1005": {
        "name": "Network Technology Foundation",
        "credits": 4,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 2,
        "category": "AI Core"
    },
    "WIA1006": {
        "name": "Machine Learning",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": True,
        "semester": 2,
        "category": "AI Core"
    },
    "WIA1007": {
        "name": "Introduction to Data Science",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 2,
        "category": "AI Core"
    },
    "WIA2001": {
        "name": "Database",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "AI Core"
    },
    "WIA2003": {
        "name": "Probability and Statistics",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": True,
        "semester": 3,
        "category": "AI Core"
    },
    "WIA2004": {
        "name": "Operating Systems",
        "credits": 4,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "AI Core"
    },
    "WIA2005": {
        "name": "Algorithm Design and Analysis",
        "credits": 4,
        "prerequisites": ["WIA1002"],
        "math_heavy": True,
        "semester": 3,
        "category": "AI Core"
    },
    "WIA2006": {
        "name": "System Analysis and Design",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "AI Core"
    },
    "WIA2007": {
        "name": "Mobile Application Development",
        "credits": 4,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "AI Core"
    }
}

# ==================== PROGRAMME CORE - COMPUTER SYSTEM & NETWORK ====================
# Source: Handbook pages 22-23

CSN_CORE = {
    "WIA1002": {
        "name": "Data Structure",
        "credits": 5,
        "prerequisites": ["WIX1002"],
        "math_heavy": False,
        "semester": 2,
        "category": "CSN Core"
    },
    "WIA1003": {
        "name": "Computer System Architecture",
        "credits": 3,
        "prerequisites": ["WIX1003"],
        "math_heavy": False,
        "semester": 2,
        "category": "CSN Core"
    },
    "WIA1005": {
        "name": "Network Technology Foundation",
        "credits": 4,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 2,
        "category": "CSN Core"
    },
    "WIA1006": {
        "name": "Machine Learning",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": True,
        "semester": 2,
        "category": "CSN Core"
    },
    "WIA2001": {
        "name": "Database",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "CSN Core"
    },
    "WIA2003": {
        "name": "Probability and Statistics",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": True,
        "semester": 3,
        "category": "CSN Core"
    },
    "WIA2004": {
        "name": "Operating Systems",
        "credits": 4,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "CSN Core"
    },
    "WIA2005": {
        "name": "Algorithm Design and Analysis",
        "credits": 4,
        "prerequisites": ["WIA1002"],
        "math_heavy": True,
        "semester": 3,
        "category": "CSN Core"
    },
    "WIA2006": {
        "name": "System Analysis and Design",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "CSN Core"
    },
    "WIA2008": {
        "name": "Advanced Network Technology",
        "credits": 4,
        "prerequisites": ["WIA1005"],
        "math_heavy": False,
        "semester": 4,
        "category": "CSN Core"
    },
    "WIA2009": {
        "name": "Digital Design and Hardware Description Language",
        "credits": 3,
        "prerequisites": ["WIA1003", "WIX1003"],
        "math_heavy": False,
        "semester": 4,
        "category": "CSN Core"
    }
}

# ==================== PROGRAMME CORE - INFORMATION SYSTEMS ====================
# Source: Handbook pages 32

IS_CORE = {
    "WIA1001": {
        "name": "Information Systems",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 2,
        "category": "IS Core"
    },
    "WIA1002": {
        "name": "Data Structure",
        "credits": 5,
        "prerequisites": ["WIX1002"],
        "math_heavy": False,
        "semester": 2,
        "category": "IS Core"
    },
    "WIA1003": {
        "name": "Computer System Architecture",
        "credits": 3,
        "prerequisites": ["WIX1003"],
        "math_heavy": False,
        "semester": 2,
        "category": "IS Core"
    },
    "WIA1005": {
        "name": "Network Technology Foundation",
        "credits": 4,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 2,
        "category": "IS Core"
    },
    "WIA1006": {
        "name": "Machine Learning",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": True,
        "semester": 2,
        "category": "IS Core"
    },
    "WIA2001": {
        "name": "Database",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "IS Core"
    },
    "WIA2003": {
        "name": "Probability and Statistics",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": True,
        "semester": 3,
        "category": "IS Core"
    },
    "WIA2004": {
        "name": "Operating Systems",
        "credits": 4,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "IS Core"
    },
    "WIA2005": {
        "name": "Algorithm Design and Analysis",
        "credits": 4,
        "prerequisites": ["WIA1002"],
        "math_heavy": True,
        "semester": 3,
        "category": "IS Core"
    },
    "WIA2006": {
        "name": "System Analysis and Design",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "IS Core"
    },
    "WIA2007": {
        "name": "Mobile Application Development",
        "credits": 4,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "IS Core"
    }
}

# ==================== PROGRAMME CORE - SOFTWARE ENGINEERING ====================
# Source: Handbook pages 37

SE_CORE = {
    "WIA1002": {
        "name": "Data Structure",
        "credits": 5,
        "prerequisites": ["WIX1002"],
        "math_heavy": False,
        "semester": 2,
        "category": "SE Core"
    },
    "WIA1003": {
        "name": "Computer System Architecture",
        "credits": 3,
        "prerequisites": ["WIX1003"],
        "math_heavy": False,
        "semester": 2,
        "category": "SE Core"
    },
    "WIA1005": {
        "name": "Network Technology Foundation",
        "credits": 4,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 2,
        "category": "SE Core"
    },
    "WIA1006": {
        "name": "Machine Learning",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": True,
        "semester": 2,
        "category": "SE Core"
    },
    "WIA2001": {
        "name": "Database",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "SE Core"
    },
    "WIA2002": {
        "name": "Software Modeling",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "SE Core"
    },
    "WIA2003": {
        "name": "Probability and Statistics",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": True,
        "semester": 3,
        "category": "SE Core"
    },
    "WIA2004": {
        "name": "Operating Systems",
        "credits": 4,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "SE Core"
    },
    "WIA2005": {
        "name": "Algorithm Design and Analysis",
        "credits": 4,
        "prerequisites": ["WIA1002"],
        "math_heavy": True,
        "semester": 3,
        "category": "SE Core"
    },
    "WIA2007": {
        "name": "Mobile Application Development",
        "credits": 4,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "SE Core"
    },
    "WIA2010": {
        "name": "Human Computer Interaction",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 2,
        "category": "SE Core"
    }
}

# ==================== PROGRAMME CORE - MULTIMEDIA COMPUTING ====================
# Source: Handbook pages 42

MM_CORE = {
    "WIA1002": {
        "name": "Data Structure",
        "credits": 5,
        "prerequisites": ["WIX1002"],
        "math_heavy": False,
        "semester": 2,
        "category": "MM Core"
    },
    "WIA1003": {
        "name": "Computer System Architecture",
        "credits": 3,
        "prerequisites": ["WIX1003"],
        "math_heavy": False,
        "semester": 2,
        "category": "MM Core"
    },
    "WIA1005": {
        "name": "Network Technology Foundation",
        "credits": 4,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 2,
        "category": "MM Core"
    },
    "WIA1006": {
        "name": "Machine Learning",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": True,
        "semester": 2,
        "category": "MM Core"
    },
    "WIA1008": {
        "name": "Fundamental of Multimedia",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 2,
        "category": "MM Core"
    },
    "WIA2001": {
        "name": "Database",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "MM Core"
    },
    "WIA2003": {
        "name": "Probability and Statistics",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": True,
        "semester": 3,
        "category": "MM Core"
    },
    "WIA2004": {
        "name": "Operating Systems",
        "credits": 4,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "MM Core"
    },
    "WIA2005": {
        "name": "Algorithm Design and Analysis",
        "credits": 4,
        "prerequisites": ["WIA1002"],
        "math_heavy": True,
        "semester": 3,
        "category": "MM Core"
    },
    "WIA2006": {
        "name": "System Analysis and Design",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "MM Core"
    },
    "WIA2007": {
        "name": "Mobile Application Development",
        "credits": 4,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "MM Core"
    }
}

# ==================== PROGRAMME CORE - DATA SCIENCE ====================
# Source: Handbook pages 48

DS_CORE = {
    "WIA1001": {
        "name": "Information Systems",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 2,
        "category": "DS Core"
    },
    "WIA1002": {
        "name": "Data Structure",
        "credits": 5,
        "prerequisites": ["WIX1002"],
        "math_heavy": False,
        "semester": 2,
        "category": "DS Core"
    },
    "WIA1003": {
        "name": "Computer System Architecture",
        "credits": 3,
        "prerequisites": ["WIX1003"],
        "math_heavy": False,
        "semester": 2,
        "category": "DS Core"
    },
    "WIA1005": {
        "name": "Network Technology Foundation",
        "credits": 4,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 2,
        "category": "DS Core"
    },
    "WIA2001": {
        "name": "Database",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "DS Core"
    },
    "WIA2002": {
        "name": "Software Modeling",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "DS Core"
    },
    "WIA2003": {
        "name": "Probability and Statistics",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": True,
        "semester": 3,
        "category": "DS Core"
    },
    "WIA2004": {
        "name": "Operating Systems",
        "credits": 4,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 3,
        "category": "DS Core"
    },
    "WID3006": {
        "name": "Machine Learning",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": True,
        "semester": 3,
        "category": "DS Core"
    },
    "WIE2003": {
        "name": "Introduction to Data Science",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "semester": 2,
        "category": "DS Core"
    }
}

# ==================== SPECIALIZATION ELECTIVES ====================

# AI Electives (Source: Handbook pages 27, 69-72)
AI_ELECTIVES = {
    "WIC2008": {
        "name": "Internet of Things",
        "credits": 3,
        "prerequisites": ["WIA1005"],
        "math_heavy": False,
        "pathway": "AI",
        "category": "AI Elective"
    },
    "WID2001": {
        "name": "Knowledge Representation and Reasoning",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "pathway": "AI",
        "category": "AI Elective"
    },
    "WID2002": {
        "name": "Computing Mathematics II",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": True,
        "pathway": "AI",
        "category": "AI Elective"
    },
    "WID2003": {
        "name": "Cognitive Science",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "pathway": "AI",
        "category": "AI Elective"
    },
    "WID3001": {
        "name": "Functional and Logic Programming",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "pathway": "AI",
        "category": "AI Elective"
    },
    "WID3002": {
        "name": "Natural Language Processing",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "pathway": "AI",
        "category": "AI Elective"
    },
    "WID3007": {
        "name": "Fuzzy Logic",
        "credits": 3,
        "prerequisites": ["WIX1001"],
        "math_heavy": True,
        "pathway": "AI",
        "category": "AI Elective"
    },
    "WID3010": {
        "name": "Autonomous Robots",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "pathway": "AI",
        "category": "AI Elective"
    },
    "WID3011": {
        "name": "Deep Learning",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": True,
        "pathway": "AI",
        "category": "AI Elective"
    },
    "WID3012": {
        "name": "Evolutionary Computation",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "pathway": "AI",
        "category": "AI Elective"
    },
    "WID3013": {
        "name": "Computer Vision and Pattern Recognition",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "pathway": "AI",
        "category": "AI Elective"
    },
    "WID3014": {
        "name": "Practical Artificial Intelligence",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "pathway": "AI",
        "category": "AI Elective"
    },
    "WID3015": {
        "name": "Numerical Analysis",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": True,
        "pathway": "AI",
        "category": "AI Elective"
    },
    "WIG3004": {
        "name": "Virtual Reality",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "pathway": "AI",
        "category": "AI Elective"
    }
}

# CSN Electives (Source: Handbook pages 63-67)
CSN_ELECTIVES = {
    "WIC2002": {"name": "Network Security", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "CSN"},
    "WIC2004": {"name": "Internet Technology", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "CSN"},
    "WIC2005": {"name": "Programmable Network", "credits": 3, "prerequisites": ["WIA2008"], "math_heavy": False, "pathway": "CSN"},
    "WIC2006": {"name": "Digital Forensic", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "CSN"},
    "WIC2007": {"name": "Cyber Security", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "CSN"},
    "WIC2008": {"name": "Internet of Things", "credits": 3, "prerequisites": ["WIA1005"], "math_heavy": False, "pathway": "CSN"},
    "WIC3001": {"name": "Mathematics in Networking", "credits": 3, "prerequisites": [], "math_heavy": True, "pathway": "CSN"},
    "WIC3002": {"name": "Cryptography", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "CSN"},
    "WIC3003": {"name": "Embedded System Programming", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "CSN"},
    "WIC3004": {"name": "Computer Penetration", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "CSN"},
    "WIC3005": {"name": "Enterprise Network Design and Management", "credits": 3, "prerequisites": ["WIA1005"], "math_heavy": False, "pathway": "CSN"},
    "WIC3006": {"name": "Mobile Computing", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "CSN"},
    "WIC3007": {"name": "Principles of Distributed System", "credits": 3, "prerequisites": ["WIA1005"], "math_heavy": False, "pathway": "CSN"},
    "WIC3008": {"name": "Microprocessor", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "CSN"},
    "WIC3009": {"name": "Parallel Programming", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "CSN"}
}

# IS Electives (Source: Handbook pages 73-77)
IS_ELECTIVES = {
    "WIC2008": {"name": "Internet of Things", "credits": 3, "prerequisites": ["WIA1005"], "math_heavy": False, "pathway": "IS"},
    "WIE2001": {"name": "Trends in Information Systems", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "IS"},
    "WIE2002": {"name": "Open-Source Programming: Application and Technology", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "IS"},
    "WIE2003": {"name": "Introduction to Data Science", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "IS"},
    "WIE2005": {"name": "Information Retrieval and Web Search", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "IS"},
    "WIE3001": {"name": "Advanced Database", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "IS"},
    "WIE3002": {"name": "Electronic Commerce", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "IS"},
    "WIE3003": {"name": "Information System Control and Security", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "IS"},
    "WIE3005": {"name": "Knowledge Management and Engineering", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "IS"},
    "WIE3006": {"name": "Information System Auditing", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "IS"},
    "WIE3007": {"name": "Data Mining and Warehousing", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "IS"},
    "WIE3010": {"name": "Data Visualization", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "IS"},
    "WIE3012": {"name": "Business Analytics and Intelligence", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "IS"},
    "WIF2003": {"name": "Web Programming", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "IS"}
}

# SE Electives (Source: Handbook pages 78-82)
SE_ELECTIVES = {
    "WIF2002": {"name": "Software Requirements Engineering", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "SE"},
    "WIF2003": {"name": "Web Programming", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "SE"},
    "WIF3001": {"name": "Software Testing", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "SE"},
    "WIF3002": {"name": "Software Process and Quality", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "SE"},
    "WIF3004": {"name": "Software Architecture and Design Paradigms", "credits": 3, "prerequisites": ["WIA2002"], "math_heavy": False, "pathway": "SE"},
    "WIF3005": {"name": "Software Maintenance and Evolution", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "SE"},
    "WIF3006": {"name": "Component Based Software Engineering", "credits": 3, "prerequisites": ["WIA2002"], "math_heavy": False, "pathway": "SE"},
    "WIF3008": {"name": "Real Time Systems", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "SE"},
    "WIF3009": {"name": "Python for Scientific Computing", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "SE"},
    "WIF3010": {"name": "Programming Language Paradigm", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "SE"},
    "WIF3011": {"name": "Concurrent and Parallel Programming", "credits": 3, "prerequisites": ["WIX1002", "WIA2004"], "math_heavy": False, "pathway": "SE"},
    "WIC2008": {"name": "Internet of Things", "credits": 3, "prerequisites": ["WIA1005"], "math_heavy": False, "pathway": "SE"},
    "WIG3005": {"name": "Game Development", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "SE"}
}

# MM Electives (Source: Handbook pages 83-87)
MM_ELECTIVES = {
    "WIG2001": {"name": "Digital Image Processing", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "MM"},
    "WIG2002": {"name": "Computer Graphics", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "MM"},
    "WIG2004": {"name": "Audio Synthesis", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "MM"},
    "WIG2005": {"name": "Interactive Design", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "MM"},
    "WIG3001": {"name": "Mathematics for Multimedia", "credits": 3, "prerequisites": [], "math_heavy": True, "pathway": "MM"},
    "WIG3002": {"name": "Rendering and Animation", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "MM"},
    "WIG3003": {"name": "Multimedia Programming", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "MM"},
    "WIG3004": {"name": "Virtual Reality", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "MM"},
    "WIG3005": {"name": "Game Development", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "MM"},
    "WIG3006": {"name": "Digital Video Processing", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "MM"},
    "WIG3007": {"name": "Special Topics in Multimedia", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "MM"},
    "WIG3008": {"name": "Multimedia Forensic and Security", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "MM"},
    "WIE3010": {"name": "Data Visualization", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "MM"},
    "WIF2003": {"name": "Web Programming", "credits": 3, "prerequisites": [], "math_heavy": False, "pathway": "MM"}
}

# ==================== DATA SCIENCE ELECTIVES ====================
# Source: Handbook pages 88-92

DS_ELECTIVES = {
    "WIG2001": {
        "name": "Digital Image Processing",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "pathway": "DS",
        "category": "DS Elective"
    },
    "WIG2002": {
        "name": "Computer Graphics",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "pathway": "DS",
        "category": "DS Elective"
    },
    "WIG2004": {
        "name": "Audio Synthesis",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "pathway": "DS",
        "category": "DS Elective"
    },
    "WIG2005": {
        "name": "Interactive Design",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "pathway": "DS",
        "category": "DS Elective"
    },
    "WIG3001": {
        "name": "Mathematics for Multimedia",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": True,
        "pathway": "DS",
        "category": "DS Elective"
    },
    "WIG3002": {
        "name": "Rendering and Animation",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "pathway": "DS",
        "category": "DS Elective"
    },
    "WIG3003": {
        "name": "Multimedia Programming",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "pathway": "DS",
        "category": "DS Elective"
    },
    "WIG3004": {
        "name": "Virtual Reality",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "pathway": "DS",
        "category": "DS Elective"
    },
    "WIG3005": {
        "name": "Game Development",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "pathway": "DS",
        "category": "DS Elective"
    },
    "WIG3006": {
        "name": "Digital Video Processing",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "pathway": "DS",
        "category": "DS Elective"
    },
    "WIE3010": {
        "name": "Data Visualization",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "pathway": "DS",
        "category": "DS Elective"
    },
    "WIF2003": {
        "name": "Web Programming",
        "credits": 3,
        "prerequisites": [],
        "math_heavy": False,
        "pathway": "DS",
        "category": "DS Elective"
    }
}

# ==================== MATH-HEAVY COURSES (For Heuristic 1) ====================

MATH_HEAVY_COURSES = [
    "WIX1001",      # Computing Mathematics I
    "WID2002",      # Computing Mathematics II
    "WID3007",      # Fuzzy Logic
    "WID3015",      # Numerical Analysis
    "WIA1006",      # Machine Learning
    "WIA2003",      # Probability and Statistics
    "WIA2005",      # Algorithm Design and Analysis
    "WID3011",      # Deep Learning
    "WIC3001",      # Mathematics in Networking
    "WIG3001",      # Mathematics for Multimedia
    "WID3006"       # Machine Learning (DS)
]

# ==================== GRADUATION REQUIREMENTS ====================

GRADUATION_REQUIREMENTS = {
    "AI": {"total_credits": 123, "faculty_core_credits": 17, "programme_core_credits": 59, "elective_credits": 30, "university_credits": 14, "min_cgpa": 2.0},
    "CSN": {"total_credits": 128, "faculty_core_credits": 17, "programme_core_credits": 59, "elective_credits": 30, "university_credits": 14, "min_cgpa": 2.0},
    "IS": {"total_credits": 128, "faculty_core_credits": 17, "programme_core_credits": 59, "elective_credits": 30, "university_credits": 14, "min_cgpa": 2.0},
    "SE": {"total_credits": 128, "faculty_core_credits": 17, "programme_core_credits": 59, "elective_credits": 30, "university_credits": 14, "min_cgpa": 2.0},
    "MM": {"total_credits": 128, "faculty_core_credits": 17, "programme_core_credits": 59, "elective_credits": 30, "university_credits": 14, "min_cgpa": 2.0},
    "DS": {"total_credits": 124, "faculty_core_credits": 17, "programme_core_credits": 63, "elective_credits": 18, "university_credits": 20, "min_cgpa": 2.0}
}

# ==================== HELPER FUNCTIONS ====================

def get_programme_core(programme):
    """Return core courses for a specific programme"""
    programme_map = {
        "AI": AI_CORE,
        "CSN": CSN_CORE,
        "IS": IS_CORE,
        "SE": SE_CORE,
        "MM": MM_CORE,
        "DS": DS_CORE
    }
    return programme_map.get(programme, {})

def get_programme_electives(programme):
    """Return electives for a specific programme"""
    elective_map = {
        "AI": AI_ELECTIVES,
        "CSN": CSN_ELECTIVES,
        "IS": IS_ELECTIVES,
        "SE": SE_ELECTIVES,
        "MM": MM_ELECTIVES,
        "DS": DS_ELECTIVES
    }
    return elective_map.get(programme, {})

def get_all_courses():
    """Return all courses from all categories"""
    all_courses = {}
    all_courses.update(FACULTY_CORE)
    all_courses.update(AI_CORE)
    all_courses.update(CSN_CORE)
    all_courses.update(IS_CORE)
    all_courses.update(SE_CORE)
    all_courses.update(MM_CORE)
    all_courses.update(DS_CORE)
    all_courses.update(AI_ELECTIVES)
    all_courses.update(CSN_ELECTIVES)
    all_courses.update(IS_ELECTIVES)
    all_courses.update(SE_ELECTIVES)
    all_courses.update(MM_ELECTIVES)
    return all_courses

def check_prerequisites(course_code, completed_courses):
    """Check if prerequisites for a course are satisfied"""
    all_courses = get_all_courses()
    
    if course_code not in all_courses:
        return False, f"Course {course_code} not found"
    
    prereqs = all_courses[course_code].get("prerequisites", [])
    missing = [p for p in prereqs if p not in completed_courses]
    
    if missing:
        return False, f"Missing prerequisites: {', '.join(missing)}"
    return True, "Prerequisites satisfied"

if __name__ == "__main__":
    print("=== Knowledge Base Loaded Successfully ===")
    print(f"Faculty Core Courses: {len(FACULTY_CORE)}")
    print(f"AI Core: {len(AI_CORE)}, AI Electives: {len(AI_ELECTIVES)}")
    print(f"CSN Core: {len(CSN_CORE)}, CSN Electives: {len(CSN_ELECTIVES)}")
    print(f"IS Core: {len(IS_CORE)}, IS Electives: {len(IS_ELECTIVES)}")
    print(f"SE Core: {len(SE_CORE)}, SE Electives: {len(SE_ELECTIVES)}")
    print(f"MM Core: {len(MM_CORE)}, MM Electives: {len(MM_ELECTIVES)}")
    print(f"DS Core: {len(DS_CORE)}")
    print(f"Total Courses: {len(get_all_courses())}")