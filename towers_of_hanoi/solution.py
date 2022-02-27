
from matplotlib.pyplot import hist

def move(origin, destination, history):
    destination.append(origin.pop())
    history.append(destination)

def hanoi(disc, source, dest = [], aux = [], history = []):
    #print("Source:", source)
    #print("Dest:", dest)
    #print("Aux:", aux)

    if disc == 1:
        move(source, dest, history)

    else:
        hanoi(disc - 1, source, aux, dest, history)
        move(source, dest, history)
        hanoi(disc - 1, aux, dest, source, history)

    #print("Result", source, aux, dest)
    #print("---------------------")
    return history

if __name__ == "__main__":
    stack = [5,4,3,2,1]
    history = hanoi(len(stack), stack)
    print(history)