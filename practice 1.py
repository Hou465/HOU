import random
y0 = 50
x0 = 50
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
if random.random() < 0.5:
    x0 -= 1
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1
print(y0,x0)