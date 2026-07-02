def get_total_bill(cart_amount:int) ->int:
    return cart_amount + 50
def test_get_total_bill():
    assert get_total_bill(100) == 150
    assert get_total_bill(0) == 50

def get_greeting(name:str) ->str:
    return f"Hello, {name}!"
def test_get_greeting():
    assert get_greeting("Nilesh") == "Hello, Nilesh!"
   

def has_free_shipping(cart_amount:float) ->bool:
    return cart_amount >= 500
def test_has_free_shipping():
    assert has_free_shipping(600) == True
    assert has_free_shipping(400.0) == False
    assert has_free_shipping(800.0) == True