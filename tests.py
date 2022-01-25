import functions 
def test_sum():
    assert functions.f1() == 6, "Should be 6"

def test_sum_tuple():
    assert functions.f2() == 6+10, "Should be 16"

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")