def calculate_score(study_hours, attendance, assignment_score):
	score = (
			(study_hours / 10) * 30 +
			(attendance / 100) * 30 +
			(assignment_score / 100) * 40
	)

	return round(score, 2)

def get_result(score):
	if score >= 50:
		return "PASS"
	else:
		return "NEEDS IMPROVEMENT"