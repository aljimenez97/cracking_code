
def multiply(x,y):
    if x == 0 or y == 0:
        return 0
    if x > y:
        return y + multiply(x-1, y)
    else:
        return x + multiply(x, y-1)

if __name__ == "__main__":
    print(multiply(7,8))