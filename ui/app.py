import streamlit as st
import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from inference.engine import InferenceEngine
from data.courses import (
    FACULTY_CORE, AI_CORE, CSN_CORE, IS_CORE, SE_CORE, MM_CORE, DS_CORE,
    AI_ELECTIVES, get_all_courses
)
from data.students import STUDENTS, get_student, get_all_students
from ui.survey import show_sus_survey

# Page configuration
st.set_page_config(
    page_title="FCSIT Course Recommendation Expert System",
    page_icon="🎓",
    layout="wide"
)

# Initialize session state
if 'recommendations_generated' not in st.session_state:
    st.session_state.recommendations_generated = False

# Title
st.title("🎓 FCSIT Expert System for Academic Course Recommendation")
st.caption("Faculty of Computer Science & Information Technology | Universiti Malaya")
st.markdown("---")

# Programme names mapping
PROGRAMME_NAMES = {
    "AI": "Bachelor of Computer Science (Artificial Intelligence)",
    "CSN": "Bachelor of Computer Science (Computer System and Network)",
    "IS": "Bachelor of Computer Science (Information Systems)",
    "SE": "Bachelor of Computer Science (Software Engineering)",
    "MM": "Bachelor of Computer Science (Multimedia Computing)",
    "DS": "Bachelor of Computer Science (Data Science)"
}

PROGRAMME_OPTIONS = ["AI", "CSN", "IS", "SE", "MM", "DS"]

# Function to get core dictionary by programme
def get_core_dict(programme):
    core_map = {
        "AI": AI_CORE,
        "CSN": CSN_CORE,
        "IS": IS_CORE,
        "SE": SE_CORE,
        "MM": MM_CORE,
        "DS": DS_CORE
    }
    return core_map.get(programme, {})

# Sidebar for student input
with st.sidebar:
    st.header("📋 Student Profile")
    
    # Option to load from database or manual input
    input_method = st.radio(
        "Input Method",
        ["Manual Input", "Load from Student Database"],
        index=0
    )
    
    if input_method == "Load from Student Database":
        student_ids = get_all_students()
        selected_id = st.selectbox("Select Student ID", student_ids)
        
        if st.button("Load Student Data"):
            student_data = get_student(selected_id)
            if student_data:
                st.session_state.loaded_student = student_data
                st.success(f"Loaded: {student_data['name']}")
                st.rerun()
        
        if 'loaded_student' in st.session_state:
            student = st.session_state.loaded_student
            st.info(f"**Loaded Student:** {student['name']}")
            st.write(f"CGPA: {student['cgpa']}")
            st.write(f"Semester: {student['semester']}")
            st.write(f"Programme: {PROGRAMME_NAMES.get(student['programme'], student['programme'])}")
            st.write(f"Completed Courses: {len(student['completed_courses'])}")
            
            # Use loaded data for inputs
            student_id = selected_id
            cgpa = student['cgpa']
            current_semester = student['semester']
            programme = student['programme']
            programme_display_value = PROGRAMME_NAMES.get(programme, programme)
            completed_courses = student['completed_courses'].copy()
            interest = student['interest']
            is_fyp_semester = student['is_fyp_semester']
            remaining_credits = student['remaining_credits']
        else:
            # Fallback to manual
            student_id = st.text_input("Student ID", placeholder="e.g., S001", value="S999")
            cgpa = st.number_input("CGPA", 0.0, 4.0, 3.2, 0.01)
            current_semester = st.selectbox("Semester", [1,2,3,4,5,6,7,8], index=3)
            programme_code = st.selectbox("Programme", PROGRAMME_OPTIONS, format_func=lambda x: PROGRAMME_NAMES[x])
            programme = programme_code
            programme_display_value = PROGRAMME_NAMES[programme_code]
            completed_courses = []
            interest = "AI / Machine Learning"
            is_fyp_semester = False
            remaining_credits = 60
    else:
        # Manual input mode
        student_id = st.text_input("Student ID", placeholder="e.g., S001", value="S999")
        cgpa = st.number_input("CGPA", 0.0, 4.0, 3.2, 0.01)
        current_semester = st.selectbox("Semester", [1,2,3,4,5,6,7,8], index=3)
        programme_code = st.selectbox("Programme", PROGRAMME_OPTIONS, format_func=lambda x: PROGRAMME_NAMES[x])
        programme = programme_code
        programme_display_value = PROGRAMME_NAMES[programme_code]
        
        st.markdown("---")
        st.subheader("✅ Completed Courses")
        
        completed_courses = []
        
        # Faculty Core Courses
        st.write("**📖 Faculty Core Courses (All Students):**")
        for code, info in FACULTY_CORE.items():
            prereq_str = ', '.join(info['prerequisites']) if info['prerequisites'] else 'None'
            
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"**{code}** - {info['name']}")
                st.caption(f"📚 Prerequisites: {prereq_str} | Credits: {info['credits']}")
            with col2:
                if st.checkbox("✓ Complete", key=f"faculty_section_{code}"):
                    completed_courses.append(code)
            st.divider()
        
        # Programme-specific courses
        st.write(f"**🎯 {PROGRAMME_NAMES[programme]} Core Courses:**")
        
        core_dict = get_core_dict(programme)
        prefix = programme.lower()
        
        for code, info in core_dict.items():
            # Skip if already in faculty core to avoid duplicates
            if code in FACULTY_CORE:
                continue
                
            prereq_str = ', '.join(info['prerequisites']) if info['prerequisites'] else 'None'
            
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"**{code}** - {info['name']}")
                st.caption(f"📚 Prerequisites: {prereq_str} | Credits: {info['credits']}")
            with col2:
                if st.checkbox("✓ Complete", key=f"{prefix}_core_section_{code}"):
                    completed_courses.append(code)
            st.divider()
        
        st.markdown("---")
        st.subheader("🎯 Interests")
        interest = st.selectbox(
            "Primary interest",
            ["AI / Machine Learning", "Networking", "Data Science", "Software Development", 
             "Cybersecurity", "Multimedia", "Information Systems"]
        )
        
        is_fyp_semester = st.checkbox("FYP Semester? (Heuristic 1 will deprioritize math-heavy courses)")
        remaining_credits = st.number_input("Remaining Credits for Graduation", 0, 128, 60)

# Main area
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📊 Current Academic Summary")
    st.metric("Student ID", student_id)
    st.metric("CGPA", f"{cgpa:.2f}")
    st.metric("Semester", current_semester)
    st.metric("Programme", programme_display_value)
    st.metric("Completed Courses", len(completed_courses))
    
    if cgpa < 2.0:
        st.warning("⚠️ GPA < 2.0 - Rule 1 active (foundation courses only)")
    if is_fyp_semester:
        st.info("💡 Heuristic 1 active: Math-heavy electives deprioritized")

with col2:
    st.subheader("📚 Completed Courses List")
    if completed_courses:
        for code in completed_courses[:10]:
            if code in FACULTY_CORE:
                st.write(f"✅ {code}: {FACULTY_CORE[code]['name']}")
            else:
                core_dict = get_core_dict(programme)
                if code in core_dict:
                    st.write(f"✅ {code}: {core_dict[code]['name']}")
                else:
                    st.write(f"✅ {code}")
        if len(completed_courses) > 10:
            st.write(f"... and {len(completed_courses) - 10} more")
    else:
        st.write("No courses selected")

# Recommendation button
st.markdown("---")
if st.button("🔍 Generate Recommendations", type="primary", use_container_width=True):
    
    student_data = {
        'cgpa': cgpa,
        'completed_courses': completed_courses,
        'interest': interest,
        'current_semester': current_semester,
        'is_fyp_semester': is_fyp_semester,
        'programme': programme,
        'remaining_credits': remaining_credits
    }
    
    engine = InferenceEngine(student_data)
    recommendations, explanations = engine.get_recommendations_with_details()
    rules_applied = engine.get_applied_rules_summary()
    
    st.session_state.recommendations_generated = True
    st.session_state.last_recommendations = recommendations
    st.session_state.last_explanations = explanations
    st.session_state.last_rules = rules_applied
    st.session_state.last_student = student_data
    
    # Display results
    st.subheader("🎯 Recommended Elective Courses")
    
    if recommendations:
        for rec in recommendations[:10]:
            st.success(f"✅ **{rec['code']}** - {rec['name']} ({rec['credits']} credits)")
    else:
        st.info("No recommendations available. Make sure you have completed some prerequisites.")
    
    with st.expander("📖 Reasoning Explanation"):
        st.markdown("#### Rules Applied:")
        
        for rule, applied in rules_applied.items():
            if applied:
                st.success(f"✅ {rule} - Applied")
            else:
                st.info(f"⏭️ {rule} - Not triggered")
        
        st.markdown("---")
        st.markdown("#### Detailed Explanations:")
        for exp in explanations[:15]:
            st.text(exp)

# Show survey if recommendations were generated
if st.session_state.recommendations_generated:
    show_sus_survey()

# Footer
st.markdown("---")
st.caption("🎓 Expert System for Academic Course Recommendation | UGHB2024/2025 FCSIT Handbook")
st.caption("Forward Chaining: Rule 5 → Rule 2 → Rule 1 → Rule 4 → Rule 3 → Heuristic 1")