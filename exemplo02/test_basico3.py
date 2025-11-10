def soma(a,b):
    return a + b

def comprimento(lista):
    return len(lista)

def test_soma():
    assert soma(1,2) == 3
    assert soma(10,-5) == 5

def test_comprimento():
    assert comprimento([1,2,3,4,5]) == 5
    assert comprimento([1,2,3,4,5,6]) == 6
