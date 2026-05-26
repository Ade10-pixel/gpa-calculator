import streamlit as st

st.set_page_config(page_title="CGPA Calculator", page_icon="🎓")

# ----------------------------
# COURSE CLASS
# ----------------------------
class Course:
    def __init__(self, course_code, unit, grade):
        self.course_code = course_code.upper()
        self.unit = unit
        self.grade = grade.upper()

    def get_grade_point(self):
        grade_point = {
            "A": 5,
            "B": 4,
            "C": 3,
            "D": 2,
            "E": 1,
            "F": 0
        }
        return grade_point.get(self.grade, 0)

    def result(self):
        return self.unit * self.get_grade_point()


# ----------------------------
# SESSION STORAGE (IMPORTANT 🔥)
# ----------------------------
if "courses" not in st.session_state:
    st.session_state.courses = []


# ----------------------------
# TITLE
# ----------------------------
st.title("🎓 CGPA Calculator App")
st.write("Add your courses and calculate CGPA instantly")

# ----------------------------
# INPUTS
# ----------------------------
course_code = st.text_input("Course Code")
unit = st.number_input("Course Unit", min_value=1, max_value=10, step=1)
grade = st.selectbox("Grade", ["A", "B", "C", "D", "E", "F"])

# ----------------------------
# ADD COURSE BUTTON
# ----------------------------
if st.button("➕ Add Course"):
    if course_code:
        new_course = Course(course_code, unit, grade)
        st.session_state.courses.append(new_course)
        st.success(f"{course_code.upper()} added!")
    else:
        st.error("Enter a course code")


# ----------------------------
# DISPLAY TABLE
# ----------------------------
st.subheader("📋 Course List")

if st.session_state.courses:
    for c in st.session_state.courses:
        st.write(
            f"**{c.course_code}** | {c.unit} Units | {c.grade} | {c.result()} Points"
        )
else:
    st.info("No courses added yet")


# ----------------------------
# CGPA CALCULATION
# ----------------------------
def calculate_cgpa(courses):
    total_units = sum(c.unit for c in courses)
    total_points = sum(c.result() for c in courses)

    if total_units == 0:
        return 0

    return total_points / total_units


# ----------------------------
# CLASSIFICATION
# ----------------------------
def get_classification(cgpa):
    if cgpa >= 4.5:
        return "First Class 🏆"
    elif cgpa >= 3.5:
        return "Second Class Upper 🎯"
    elif cgpa >= 2.4:
        return "Second Class Lower 🙂"
    elif cgpa >= 1.5:
        return "Third Class 😐"
    elif cgpa >= 1.0:
        return "Pass 😬"
    else:
        return "Fail 💀"


# ----------------------------
# RESULTS
# ----------------------------
if st.session_state.courses:
    cgpa = calculate_cgpa(st.session_state.courses)
    st.subheader("📊 Result")
    st.metric("CGPA", round(cgpa, 2))
    st.write("Classification:", get_classification(cgpa))


# ----------------------------
# RESET BUTTON
# ----------------------------
if st.button("🧹 Reset All"):
    st.session_state.courses = []
    st.success("Reset successful!")
