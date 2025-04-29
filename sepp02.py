ID = {"p001" : 1500,
    "p002" : 1432,
    "p003" : 6756
    }
def get_bill(patient_ID):
    if patient_ID in ID:
        return ID[patient_ID]
    return "ID not found"

def pay_bill(amount,upi_ID):
    if "@" not in upi_ID:
        return "Invalid UPI id"
    if amount > 0:
        return "Payment successful"
    return "Invalid amount"


# if __name__=='__main__':
#     patient_id = "p003"
#     print(get_bill(patient_id))
#     amount = 20000
#     id = "abcde@ybl"
#     print(pay_bill(amount,id))

