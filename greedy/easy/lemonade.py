
# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. 
# You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
def lemonade(bills):
    change = {
        5: 0,
        10: 0,
        20: 0,
    }

    for bill in bills:
        change[bill] += 1

        if bill == 10:
            if change[5] >= 0:
                change[5] -= 1
                continue
            return False
        
        if bill == 20:
            if change[10] > 0 and change[5] > 0:
                change[10] -= 1
                change[5] -= 1
                continue
            if change[5] >= 3:
                change[5] -= 3
                continue
            return False

    return True


if __name__ == "__main__":
    bills = [5,5,5,10,20]
    print(lemonade(bills))