
def count_one_bits(number):
    return bin(number).count("1")

if __name__ == "__main__":
    number = 8
    print(count_one_bits(number))