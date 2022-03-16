from exercise4 import SumGeometricElements

def test_SumGeometricElements():
    assert SumGeometricElements(100, 0.5, 20) == 175.0
    assert SumGeometricElements(200, 0.25, 10) == 262.5
    assert SumGeometricElements(30, 0.75, 8) == 91.5234375
    assert SumGeometricElements(300, 0.5, 30) == 562.5
    assert SumGeometricElements(10, 0.2, 0.5) == 12.0