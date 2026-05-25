from yahtzee_backend import *

def test_score_short_straight():
    score = score_short_straight([1,2,3,4,6])
    assert score == 30