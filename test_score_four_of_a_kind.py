from yahtzee_backend import *

def test_score_four_of_a_kind():
    score = score_4_of_a_kind( [1,1,1,1,6])
    assert score == 10