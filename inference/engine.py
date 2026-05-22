# inference/engine.py - Updated for all programmes
from data.courses import (
    get_programme_electives, get_programme_core, 
    MATH_HEAVY_COURSES, check_prerequisites, FACULTY_CORE
)

class InferenceEngine:
    def __init__( self, student_data):
        """
        Initialize inference engine with student data
        student_data = {
            'cgpa': float,
            'completed_courses': list,
            'interest': str,
            'current_semester': int,
            'is_fyp_semester': bool,
            'programme': str,  # AI, CSN, IS, SE, MM, DS
            'remaining_credits': int
        }
        """
        self.student = student_data
        self.recommendations = []
        self.explanations = []
        self.facts = set(student_data.get('completed_courses', []))
        self.rules_fired = []
        
    def apply_rules(self):
        """Apply all rules in priority order (forward chaining)"""
        
        # Priority order from PDF Page 7:
        # Rule 5 > Rule 2 > Rule 1 > Rule 4 > Rule 3 > Heuristic 1
        
        programme = self.student.get('programme', 'AI')
        
        # Get electives for this programme
        electives = get_programme_electives(programme)
        
        if not electives:
            self.explanations.append(f"No electives defined for programme {programme}")
            return [], self.explanations
        
        processed = set()
        
        for course_code, course_info in electives.items():
            if course_code in processed:
                continue
                
            # === RULE 5: Conflict Avoidance (Highest Priority) ===
            if course_code in self.facts:
                self.explanations.append(f"❌ {course_code}: Already taken (Rule 5 - Conflict Avoidance)")
                continue
                
            # === RULE 2: Prerequisite Check ===
            prereq_ok, prereq_msg = check_prerequisites(course_code, self.facts)
            if not prereq_ok:
                self.explanations.append(f"❌ {course_code}: {prereq_msg} (Rule 2 - Prerequisite)")
                continue
                
            # === RULE 1: Low GPA Safety Gate ===
            if self.student['cgpa'] < 2.0:
                self.explanations.append(f"⚠️ GPA {self.student['cgpa']} < 2.0 - Foundation courses only (Rule 1)")
                continue
                
            # === RULE 4: Graduation Requirement Filter ===
            if self.student.get('remaining_credits', 100) <= 20:
                self.recommendations.append(course_code)
                self.explanations.append(f"✅ {course_code}: Graduation requirement (Rule 4 - Remaining credits: {self.student['remaining_credits']})")
                processed.add(course_code)
                continue
                
            # === RULE 3: Interest Path ===
            interest = self.student.get('interest', '')
            course_pathway = course_info.get('pathway', '')
            
            # Simple interest matching
            if interest.lower() in course_info['name'].lower() or interest.lower() in str(course_pathway).lower():
                self.recommendations.append(course_code)
                self.explanations.append(f"✅ {course_code}: Matches your interest '{interest}' (Rule 3 - Interest Path)")
                processed.add(course_code)
                continue
                
            # === HEURISTIC 1: Expert Advice - Avoid math-heavy during FYP ===
            if self.student.get('is_fyp_semester', False):
                if course_code in MATH_HEAVY_COURSES or course_info.get('math_heavy', False):
                    self.explanations.append(f"⚠️ {course_code}: Deprioritized (math-heavy during FYP - Heuristic 1)")
                    continue
                    
            # Default: course is eligible
            self.recommendations.append(course_code)
            self.explanations.append(f"✅ {course_code}: Recommended based on your profile")
            processed.add(course_code)
            
        return self.recommendations, self.explanations
    
    def get_recommendations_with_details(self):
        """Get recommendations with full course details"""
        from data.courses import get_programme_electives, FACULTY_CORE, get_programme_core
        
        programme = self.student.get('programme', 'AI')
        electives = get_programme_electives(programme)
        core_courses = get_programme_core(programme)
        
        recommendations, explanations = self.apply_rules()
        
        detailed = []
        for course_code in recommendations:
            if course_code in electives:
                course = electives[course_code]
            elif course_code in core_courses:
                course = core_courses[course_code]
            elif course_code in FACULTY_CORE:
                course = FACULTY_CORE[course_code]
            else:
                continue
                
            detailed.append({
                "code": course_code,
                "name": course["name"],
                "credits": course["credits"],
                "math_heavy": course.get("math_heavy", False),
                "prerequisites": course.get("prerequisites", [])
            })
            
        return detailed, explanations
    
    def get_applied_rules_summary(self):
        """Return which rules were applied for reporting"""
        rules = {
            "Rule 1 (Low GPA Safety Gate)": self.student['cgpa'] < 2.0,
            "Rule 2 (Prerequisite Check)": True,
            "Rule 3 (Interest Path)": self.student.get('interest') is not None,
            "Rule 4 (Graduation Filter)": self.student.get('remaining_credits', 100) <= 20,
            "Rule 5 (Conflict Avoidance)": True,
            "Heuristic 1 (FYP Math Avoidance)": self.student.get('is_fyp_semester', False)
        }
        return rules


# Test the engine
if __name__ == "__main__":
    # Test with AI student
    test_ai = {
        'cgpa': 3.2,
        'completed_courses': ['WIX1001', 'WIX1002', 'WIA1005'],
        'interest': 'Machine Learning',
        'current_semester': 4,
        'is_fyp_semester': False,
        'programme': 'AI',
        'remaining_credits': 60
    }
    
    engine = InferenceEngine(test_ai)
    recs, explanations = engine.get_recommendations_with_details()
    
    print("=== AI Programme Test ===")
    print(f"Recommendations: {len(recs)}")
    for rec in recs[:5]:
        print(f"  {rec['code']}: {rec['name']}")
    
    # Test with CSN student
    test_csn = {
        'cgpa': 3.0,
        'completed_courses': ['WIX1001', 'WIX1002', 'WIA1005'],
        'interest': 'Network Security',
        'current_semester': 4,
        'is_fyp_semester': False,
        'programme': 'CSN',
        'remaining_credits': 60
    }
    
    engine2 = InferenceEngine(test_csn)
    recs2, _ = engine2.get_recommendations_with_details()
    
    print(f"\n=== CSN Programme Test ===")
    print(f"Recommendations: {len(recs2)}")
    for rec in recs2[:5]:
        print(f"  {rec['code']}: {rec['name']}")