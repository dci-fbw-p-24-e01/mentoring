# Algorithmic Thinking

# Big O Notation

'''

O(1)
O(n)
O(log(n))
O(nlog(n))
O(n**2)
O(2**n)

'''
import numpy as np

n = np.linspace(1, 100, 500)

o_1 = np.ones_like(n)

o_n = n

o_log_n = np.log(n)

o_n_log_n = n * np.log(n)

o_n_2 = n ** 2

o_2_n = 2 ** n


# my_list = [2, 5, 8, 3, 1, 10,.............]

# my_list[0]

'''
O(1) + O(n) + Olog(n) + O(n^2)


O(n^2)

'''

# for i in my_list:
#     total = 0
#     total += i

# def binary_search(my_list, target):


# for i in my_list:
#     for j in my_list:
#         print(i, j)


# print(n)
# print(o_1)
# print(o_log_n)
# print(o_n_log_n)
# print(o_2_n)


import matplotlib.pyplot as plt

plt.figure(figsize=(20, 16))

plt.plot(n, o_1, label='O(1)')
plt.plot(n, o_n, label='O(n)')
plt.plot(n, o_log_n, label='O(log(n))')
plt.plot(n, o_n_log_n, label='nO(log(n))')
plt.plot(n, o_n_2, label='O(n^2)')
plt.plot(n, o_2_n, label='O(2^n)')

plt.xlabel('Sample size (n)')
plt.ylabel('Operations')
plt.legend()
plt.ylim(0, 100)
plt.show()




