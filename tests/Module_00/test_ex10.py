""" Tests for M0E10 loading.py => progress bar printed to stdout """
from time import sleep
from Module_00.ex_10.loading import ft_progress

# Each of these inputs is valid and should not produce any error

# X = range(100)
# X = range(100, 200)
# X = range(1)
# X = range(4)
# X = range(0, -100, -1)
# X = range(3333)

# You can also have fun changing ret and sleep time if you want, will work as well.

X = range(100)

RET = 0
for elem in ft_progress(X):
    RET += (elem + 3) % 5
    sleep(0.01)
    print()
    print(RET)
