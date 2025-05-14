from typing import List
def lemonadeChange(bills: List[int]) -> bool:
    """
    At a lemonade stand, each lemonade costs $5. 
    Customers can only pay with $5, $10, or $20 bills. 
    When a customer pays with a $10 bill, the cashier must provide $5 in change. 
    For a $20 bill, the cashier must provide $15 in change, which can be done using one of the following combinations:
    - One $10 bill and one $5 bill.
    - Three $5 bills.
    
    Given an integer array bills where bills[i] is the bill that the i-th customer pays, 
    return true if the cashier can provide every customer with the correct change, or false otherwise.
    """
    five = 0
    ten = 0

    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five > 0:
                five -= 1
                ten += 1
            else:
                return False
        else:  # bill == 20
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False

    return True