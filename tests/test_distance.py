from mlproject.distance import haversine

def test_haversine_function():
    assert type(haversine(2.380009, 48.865070, 103.852504, 1.284981)) == float
