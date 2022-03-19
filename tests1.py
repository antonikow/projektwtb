import functions 
def test_function1():
    assert functions.f1() == 5, "Should be 5"

def test_function2():
    assert functions.f2() == 15, "Should be 15"

if __name__ == "__main__":
    test_function1()
    test_function2()
    print("Everything passed OR NOT ???")