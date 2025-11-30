import random
import math

def hill_climbing(f, x_range, max_iter= 100):
    current = random.choice(list(x_range))
    for i in range(max_iter):
        neighbours = neighbourfn(current)
        nextn = max(neighbours, key = lambda x:f(x))
        if f(nextn) <= f(current):
            continue
        current = nextn
    return current, f(current)

def gen():
    exp = input("f(x): ")
    def f(x):
        return eval(exp, {"x":x, "math": math})
    return f

def neighbourfn(x):
    return [x-0.1, x, x+0.1]

def frange(start, stop, step):
    while start <= stop:
        yield start
        start += step

if __name__ == "__main__":
    f = gen()
    start, stop, step = map(float, input("Enter the range (start, stop, step size): ").split())
    x_range = [round(x,2) for x in frange(start, stop, step)]
    x, fx = hill_climbing(f, x_range)
    print(f"x: {round(x, 2)}")
    print(f"f(x): {round(fx,2)}")