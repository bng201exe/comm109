from yahtzee_backend import *


def test_score_full_house():
    score = score_full_house( [1,2,2,1,1])
    assert score == 20


