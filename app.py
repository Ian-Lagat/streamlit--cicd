import streamlit as st
from calculator import calculate_score, get_result

st.set_page_config(
	page_title = "Student Perfomance predictor",
	page_icon = "🎓"
	)

st.title("🎓 Student Perfomance Predictor")

st.write(
	"Enter the student's information below to calculate "
	"their perfomance."
)

student_name = st.text_input("Studenr Name")

study_hours = st.number_input(
	"Study Hours per day",
	min_value = 0.0,
	max_value = 10.0,
	value = 5.0
)

attendance = st.number_input(
	"Attendance (%)",
	min_value = 0.0,
	max_value = 100.0,
	value = 80.0
)

assignment_score = st.number_input(
	"Assignment Score(%)",
	min_value = 0.0,
	max_value = 100.0,
	value = 70.0
)

if st.button("Calculate Perfomance"):

	if student_name =="":
		st.warning("Please enter the student's name.")
	else:
		score = calculate_score(
			study_hours,
			attendance,
			assignment_score
		)
	result = get_result(score)

	st.subheader(f"Results for {student_name}")

	st.metric(
		"Perfomance Score",
		f"{score}%"
	)
	
	if result == "PASS":
		st.success("PASS 🍾")
	else:
		st.warning("NEEDS IMPROVEMENT ⚠️")