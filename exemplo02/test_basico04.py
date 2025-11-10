from funcoes import *

def test_email_valido():
    assert email_valido("alexsousa@gmail.com") is True

def test_dividir():
    assert dividir(5,5) == 1
    assert dividir(5,0) is None