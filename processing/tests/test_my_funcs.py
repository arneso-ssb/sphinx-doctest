from processing.src.my_funcs import circle_area


def test_circle_area():
    assert circle_area(2) < 13
    assert circle_area(2) > 12
