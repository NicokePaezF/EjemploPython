def make_multiplier(x):
    def multiplier(n):
        return x * n

    return multiplier


times10 = make_multiplier(10)
time4 = make_multiplier(4)

print(times10(3))
print(time4(5))
print(times10(time4(2)))
