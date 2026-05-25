from yahtzee_backend import *

def test_score_chance():
    score = score_chance([1,2,3,4,4])
    assert score == 14