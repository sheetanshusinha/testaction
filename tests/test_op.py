from src.maths_op import add,sub
def test_add():
    assert add(2,3)==5
    assert add(10,5)==15

def test_sub():
    assert sub(3,2)==1
    assert sub(5,1)==4