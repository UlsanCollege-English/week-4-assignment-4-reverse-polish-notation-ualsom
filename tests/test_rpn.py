from src.rpn import eval_rpn

def test_examples():
    assert eval_rpn(["2","1","+","3","*"]) == 9
    assert eval_rpn(["4","13","5","/","+"]) == 6
    assert eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22

def test_negatives_and_div():
    assert eval_rpn(["-7","3","/"]) == -2
    assert eval_rpn(["7","-3","/"]) == -2

def test_edge_single_number_only():
    assert eval_rpn(["42"]) == 42

def test_edge_large_negative_and_truncation_mix():
    assert eval_rpn(["-7","3","/","5","*","1","+"]) == -9

def test_long_expression_mixed_ops():
    tokens = ["15","7","1","1","+","-","/","3","*","2","1","1","+","+","-"]
    assert eval_rpn(tokens) == 5
