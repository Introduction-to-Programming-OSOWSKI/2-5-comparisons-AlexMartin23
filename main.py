def greaterThan(x, y):
    if x > y:
        return True
    else:
        return False

def lessThan(x, y):
    if x < y:
        return True
    else:
        return False

def equalTo(x, y):
    if x == y:
        return True
    else:
        return False

def greaterOrEqual(x, y):
    if x >= y:
        return True
    else:
        return False

def lessOrEqual(x, y):
    if x <= y:
        return True
    else:
        return False


print(greaterThan(2, 1))

print(lessThan(1, 2))

print(equalTo(1, 1))

print(greaterOrEqual(1, 1))

print(lessOrEqual(1, 1))