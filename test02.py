import sepp02 as s2

def test_get_bill():
    assert s2.get_bill("p006") == "ID not found"

def test_pay_bill():
    assert s2.pay_bill(20000,"abcde@ybl") == "Payment successful"

def test_pay_bill_invalid():
    assert s2.pay_bill(30000, "abcdefghi") == "Invalid UPI id"