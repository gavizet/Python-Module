from Module_00.ex_10.loading import ft_progress

X = range(100)

listy = range(X)

ret = 0
for elem in ft_progress(listy):
ret += (elem + 3) % 5
sleep(0.01)
print()
print(ret)