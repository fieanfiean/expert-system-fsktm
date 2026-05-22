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

# ========== INITIALIZE SESSION STATE WITH NULL VALUES ==========
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.student_id = ""
    st.session_state.cgpa = None
    st.session_state.semester = None
    st.session_state.programme = None
    st.session_state.programme_display = ""
    st.session_state.completed_courses = []
    st.session_state.interest = None
    st.session_state.is_fyp_semester = False
    st.session_state.remaining_credits = None
    st.session_state.recommendations_generated = False
    st.session_state.loaded_student = None
    st.session_state.input_method = "Manual Input"
    st.session_state.last_recommendations = []
    st.session_state.last_explanations = []
    st.session_state.last_rules = {}
    st.session_state.last_student = {}

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

# Function to reset manual inputs
def reset_manual_inputs():
    st.session_state.student_id = ""
    st.session_state.cgpa = None
    st.session_state.semester = None
    st.session_state.programme = None
    st.session_state.programme_display = ""
    st.session_state.completed_courses = []
    st.session_state.interest = None
    st.session_state.is_fyp_semester = False
    st.session_state.remaining_credits = None
    st.session_state.recommendations_generated = False

# Sidebar for student input
with st.sidebar:
    st.header("📋 Student Profile")
    
    # Reset button
    if st.button("🔄 Reset All Fields", use_container_width=True):
        reset_manual_inputs()
        st.session_state.loaded_student = None
        st.session_state.input_method = "Manual Input"
        st.rerun()
    
    st.markdown("---")
    
    # Option to load from database or manual input
    input_method = st.radio(
        "Input Method",
        ["Manual Input", "Load from Student Database"],
        index=0 if st.session_state.input_method == "Manual Input" else 1,
        key="input_method_radio"
    )
    st.session_state.input_method = input_method
    
    if input_method == "Load from Student Database":
        student_ids = get_all_students()
        selected_id = st.selectbox("Select Student ID", student_ids, index=None, placeholder="Choose a student...")
        
        if selected_id and st.button("Load Student Data", use_container_width=True):
            student_data = get_student(selected_id)
            if student_data:
                st.session_state.loaded_student = student_data
                st.session_state.student_id = selected_id
                st.session_state.cgpa = student_data['cgpa']
                st.session_state.semester = student_data['semester']
                st.session_state.programme = student_data['programme']
                st.session_state.programme_display = PROGRAMME_NAMES.get(student_data['programme'], student_data['programme'])
                st.session_state.completed_courses = student_data['completed_courses'].copy()
                st.session_state.interest = student_data['interest']
                st.session_state.is_fyp_semester = student_data['is_fyp_semester']
                st.session_state.remaining_credits = student_data['remaining_credits']
                st.success(f"✅ Loaded: {student_data['name']}")
                st.rerun()
        
        # Display loaded data
        if st.session_state.loaded_student:
            st.info(f"**Loaded Student:** {st.session_state.loaded_student['name']}")
            st.write(f"📊 CGPA: {st.session_state.cgpa}")
            st.write(f"📚 Semester: {st.session_state.semester}")
            st.write(f"🎯 Programme: {st.session_state.programme_display}")
            st.write(f"✅ Completed Courses: {len(st.session_state.completed_courses)}")
    else:
        # Manual input mode with NULL defaults
        st.write("**Enter Student Information:**")
        
        student_id = st.text_input(
            "Student ID", 
            placeholder="e.g., S001", 
            value=st.session_state.student_id if st.session_state.student_id else ""
        )
        
        cgpa = st.number_input(
            "CGPA", 
            min_value=0.0, 
            max_value=4.0, 
            value=st.session_state.cgpa if st.session_state.cgpa is not None else 0.0,
            step=0.01,
            placeholder="Enter CGPA (0.0 - 4.0)"
        )
        
        semester = st.selectbox(
            "Semester", 
            [1, 2, 3, 4, 5, 6, 7, 8], 
            index=st.session_state.semester - 1 if st.session_state.semester is not None else None,
            placeholder="Select semester"
        )
        
        programme_code = st.selectbox(
            "Programme", 
            PROGRAMME_OPTIONS, 
            index=PROGRAMME_OPTIONS.index(st.session_state.programme) if st.session_state.programme in PROGRAMME_OPTIONS else None,
            placeholder="Select programme",
            format_func=lambda x: PROGRAMME_NAMES[x]
        )
        
        # Store values in session state as user types
        if student_id:
            st.session_state.student_id = student_id
        if cgpa > 0:
            st.session_state.cgpa = cgpa
        if semester:
            st.session_state.semester = semester
        if programme_code:
            st.session_state.programme = programme_code
            st.session_state.programme_display = PROGRAMME_NAMES[programme_code]
        
        st.markdown("---")
        st.subheader("✅ Completed Courses")
        
        completed_courses = []
        
        # Only show course selection if programme is selected
        if st.session_state.programme:
            # Faculty Core Courses
            st.write("**📖 Faculty Core Courses (All Students):**")
            for code, info in FACULTY_CORE.items():
                prereq_str = ', '.join(info['prerequisites']) if info['prerequisites'] else 'None'
                
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.write(f"**{code}** - {info['name']}")
                    st.caption(f"📚 Prerequisites: {prereq_str} | Credits: {info['credits']}")
                with col2:
                    is_checked = code in st.session_state.completed_courses
                    if st.checkbox("✓ Complete", key=f"faculty_section_{code}", value=is_checked):
                        completed_courses.append(code)
                st.divider()
            
            # Programme-specific courses
            st.write(f"**🎯 {PROGRAMME_NAMES[st.session_state.programme]} Core Courses:**")
            
            core_dict = get_core_dict(st.session_state.programme)
            prefix = st.session_state.programme.lower()
            
            for code, info in core_dict.items():
                if code in FACULTY_CORE:
                    continue
                    
                prereq_str = ', '.join(info['prerequisites']) if info['prerequisites'] else 'None'
                
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.write(f"**{code}** - {info['name']}")
                    st.caption(f"📚 Prerequisites: {prereq_str} | Credits: {info['credits']}")
                with col2:
                    is_checked = code in st.session_state.completed_courses
                    if st.checkbox("✓ Complete", key=f"{prefix}_core_section_{code}", value=is_checked):
                        completed_courses.append(code)
                st.divider()
            
            st.session_state.completed_courses = completed_courses
            
            st.markdown("---")
            st.subheader("🎯 Interests")
            interest = st.selectbox(
                "Primary interest",
                ["AI / Machine Learning", "Networking", "Data Science", "Software Development", 
                 "Cybersecurity", "Multimedia", "Information Systems"],
                index=0
            )
            st.session_state.interest = interest
            
            is_fyp_semester = st.checkbox(
                "FYP Semester? (Heuristic 1 will deprioritize math-heavy courses)",
                value=st.session_state.is_fyp_semester
            )
            st.session_state.is_fyp_semester = is_fyp_semester
            
            remaining_credits = st.number_input(
                "Remaining Credits for Graduation", 
                min_value=0, 
                max_value=128, 
                value=st.session_state.remaining_credits if st.session_state.remaining_credits is not None else 60
            )
            st.session_state.remaining_credits = remaining_credits
        else:
            st.info("👈 Please select a programme first to see course options")

# Main area - Only show if data is entered
col1, col2 = st.columns([1, 1])

# Check if we have valid data to display
has_valid_data = (st.session_state.cgpa is not None and 
                  st.session_state.cgpa > 0 and 
                  st.session_state.semester is not None and 
                  st.session_state.programme is not None)

if has_valid_data:
    with col1:
        st.subheader("📊 Current Academic Summary")
        st.metric("Student ID", st.session_state.student_id if st.session_state.student_id else "Not set")
        st.metric("CGPA", f"{st.session_state.cgpa:.2f}")
        st.metric("Semester", st.session_state.semester)
        st.metric("Programme", st.session_state.programme_display)
        st.metric("Completed Courses", len(st.session_state.completed_courses))
        
        if st.session_state.cgpa < 2.0:
            st.warning("⚠️ GPA < 2.0 - Rule 1 active (foundation courses only)")
        if st.session_state.is_fyp_semester:
            st.info("💡 Heuristic 1 active: Math-heavy electives deprioritized")

    with col2:
        st.subheader("📚 Completed Courses List")
        if st.session_state.completed_courses:
            for code in st.session_state.completed_courses[:10]:
                if code in FACULTY_CORE:
                    st.write(f"✅ {code}: {FACULTY_CORE[code]['name']}")
                else:
                    core_dict = get_core_dict(st.session_state.programme)
                    if code in core_dict:
                        st.write(f"✅ {code}: {core_dict[code]['name']}")
                    else:
                        st.write(f"✅ {code}")
            if len(st.session_state.completed_courses) > 10:
                st.write(f"... and {len(st.session_state.completed_courses) - 10} more")
        else:
            st.write("No courses selected yet")
else:
    with col1:
        st.info("👈 Please enter your student information in the sidebar to get started")
    with col2:
        st.empty()

# Recommendation button
st.markdown("---")

if has_valid_data:
    if st.button("🔍 Generate Recommendations", type="primary", use_container_width=True):
        
        student_data = {
            'cgpa': st.session_state.cgpa,
            'completed_courses': st.session_state.completed_courses,
            'interest': st.session_state.interest,
            'current_semester': st.session_state.semester,
            'is_fyp_semester': st.session_state.is_fyp_semester,
            'programme': st.session_state.programme,
            'remaining_credits': st.session_state.remaining_credits
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
            st.markdown("#### Rules Applied (Priority Order from PDF Page 7):")
            
            for rule, applied in rules_applied.items():
                if applied:
                    st.success(f"✅ {rule} - Applied")
                else:
                    st.info(f"⏭️ {rule} - Not triggered")
            
            st.markdown("---")
            st.markdown("#### Detailed Explanations:")
            for exp in explanations[:15]:
                st.text(exp)
else:
    st.info("⚠️ Please fill in all required fields in the sidebar (Student ID, CGPA, Semester, Programme) to generate recommendations")

# Show survey if recommendations were generated
if st.session_state.recommendations_generated:
    show_sus_survey()

# Footer
st.markdown("---")
st.caption("🎓 Expert System for Academic Course Recommendation | UGHB2024/2025 FCSIT Handbook")
st.caption("Forward Chaining: Rule 5 → Rule 2 → Rule 1 → Rule 4 → Rule 3 → Heuristic 1")