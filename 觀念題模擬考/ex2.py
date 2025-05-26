def f(x):
    if x == 0: return 0
    if x == 1: return 1
    return f(x-1) + f(x-2)

print(f(3)+f(6)+f(8))