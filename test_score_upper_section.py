from yahtzee_backend import *

def test_score_upper_section():
    score = score_upper_section(2,2,3,3,5)
    assert score == 4