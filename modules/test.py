
def test_model_validator():
    from validators import return_model_kkt
    assert return_model_kkt(["1111110038011111","1111110028001111","1111110038011111","1111110028001111"]) == ["netpay","payonline","netpay","payonline"], "test passed"
    assert return_model_kkt(["1111110038011111","1111110028001111","1111110038011111","1111110028001111"]) != ["netpay","payonline","netpay","payonline","netpay"], "test failed"
    assert return_model_kkt(["111111003dfdf","1111110028001111","1111110038011111","1111110028001111"]) == ["len not 16","payonline","netpay","payonline"], "test passed"
    assert return_model_kkt(["111111003dfdf","1111110028001111","1111110038011111","1111110028001111"]) != ["len not 16","payonline","netpay","payonline","netpay"], "test failed"
    
print(test_model_validator())
