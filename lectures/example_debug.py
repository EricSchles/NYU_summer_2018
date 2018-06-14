import code

def function_one(x, y):
    x = 0
    y = 0
    return x/y


def function_two(x):
    x += 0.1
    for i in range(x):
        print(i)
    return x+27


def adder(x, y):
    x = int(x)
    return x + y
    
if __name__ == '__main__':
    print(function_one(5,6))
    print(function_two(5))
    print(adder(5, 8))
    print(adder(5.5, 8))
