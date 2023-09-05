import re

s = "Welcome to   regex programming   using    python"
result = re.split('\s', s)
print(result)


s = "Welcome to   regex programming   using    python"
result = re.split('\s+', s)
print(result)

s = "Welcome to   regex programming   using    python"
result = re.split('s+', s)
print(result)


s = "Welcome to   regex programming9 using7 python3"
result = re.split(r'[a-f][l-m]', s)
print(result)

# [a-m] = a, b, c, d, e, f
# [l-n] = l, m, n
# al, am, an, bl, bm, bn, cl, cm, cn and so on...