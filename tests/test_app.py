
from health_answers import get_health_answer


def test_water_question():
    answer = get_health_answer("What are the benefits of drinking water?")
    assert "water" in answer.lower()


def test_sleep_question():
    answer = get_health_answer("How can I improve my sleep?")
    assert "sleep" in answer.lower()


def test_unknown_question():
    answer = get_health_answer("What is the weather like?")
    assert "predefined answer" in answer.lower()
