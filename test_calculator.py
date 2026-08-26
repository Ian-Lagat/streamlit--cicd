from calculator import calculate_score, get_result

def test_calculate_score():
	score = calculate_score(10, 100, 100)

	assert score == 100

def test_pass_result():
	result = get_result(75)

	assert result == "PASS"

def test_fail_result():
	result = get_result(40)

	assert result == "NEEDS IMPROVEMENT"