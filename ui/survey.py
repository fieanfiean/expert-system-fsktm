# ui/survey.py
# System Usability Scale (SUS) Survey for UX Metrics

import streamlit as st

def show_sus_survey():
    """Display SUS survey after user uses the system"""
    
    st.markdown("---")
    st.subheader("📝 System Usability Scale (SUS) Survey")
    st.caption("Please rate your experience with the Expert System (1 = Strongly Disagree, 5 = Strongly Agree)")
    
    # SUS Questions (standard 10 questions)
    sus_questions = {
        "Q1": "I think that I would like to use this system frequently",
        "Q2": "I found the system unnecessarily complex",
        "Q3": "I thought the system was easy to use",
        "Q4": "I think that I would need the support of a technical person to be able to use this system",
        "Q5": "I found the various functions in this system were well integrated",
        "Q6": "I thought there was too much inconsistency in this system",
        "Q7": "I would imagine that most people would learn to use this system very quickly",
        "Q8": "I found the system very cumbersome to use",
        "Q9": "I felt very confident using the system",
        "Q10": "I needed to learn a lot of things before I could get going with this system"
    }
    
    # Store responses in session state
    if 'survey_responses' not in st.session_state:
        st.session_state.survey_responses = {}
    
    # Display questions with radio buttons
    cols = st.columns(2)
    for i, (q_id, question) in enumerate(sus_questions.items()):
        with cols[i % 2]:
            response = st.radio(
                question,
                options=[1, 2, 3, 4, 5],
                index=2,
                key=f"sus_{q_id}",
                horizontal=True,
                format_func=lambda x: ["1", "2", "3", "4", "5"][x-1]
            )
            st.session_state.survey_responses[q_id] = response
    
    # Submit button
    if st.button("Submit Survey Feedback", type="primary"):
        score = calculate_sus_score(st.session_state.survey_responses)
        
        st.success(f"✅ Thank you for your feedback!")
        st.metric("SUS Score", f"{score:.1f}", help="SUS scores above 68 are considered above average")
        
        # Interpretation
        if score >= 80:
            st.balloons()
            st.info("🌟 Excellent! Your feedback indicates high usability.")
        elif score >= 68:
            st.info("👍 Good! The system has acceptable usability.")
        elif score >= 50:
            st.warning("⚠️ Marginal. Some improvements needed.")
        else:
            st.error("❌ Poor usability. Major improvements needed.")
        
        # Store in session for report generation
        st.session_state.survey_completed = True
        st.session_state.sus_score = score
        
        return score
    return None

def calculate_sus_score(responses):
    """
    Calculate SUS score from responses
    SUS formula: 
    - Odd questions: (response - 1) * 2.5
    - Even questions: (5 - response) * 2.5
    Sum all and multiply by 2.5
    """
    total = 0
    
    # Q1, Q3, Q5, Q7, Q9 (positive - subtract 1)
    positive_q = [1, 3, 5, 7, 9]
    # Q2, Q4, Q6, Q8, Q10 (negative - subtract from 5)
    negative_q = [2, 4, 6, 8, 10]
    
    for q_num in positive_q:
        q_key = f"Q{q_num}"
        if q_key in responses:
            total += responses[q_key] - 1
    
    for q_num in negative_q:
        q_key = f"Q{q_num}"
        if q_key in responses:
            total += 5 - responses[q_key]
    
    # Multiply by 2.5 to get score out of 100
    score = total * 2.5
    return score

def get_survey_summary():
    """Return summary of survey results for report"""
    if 'survey_responses' in st.session_state and st.session_state.survey_responses:
        return {
            "responses": st.session_state.survey_responses,
            "score": st.session_state.get('sus_score', 0),
            "completed": st.session_state.get('survey_completed', False)
        }
    return None

if __name__ == "__main__":
    # Test the survey
    test_responses = {
        "Q1": 4, "Q2": 2, "Q3": 4, "Q4": 2, "Q5": 4,
        "Q6": 1, "Q7": 4, "Q8": 2, "Q9": 4, "Q10": 2
    }
    score = calculate_sus_score(test_responses)
    print(f"Test SUS Score: {score}")
    print("Expected range: 68-80 for good usability")