# -*- coding: utf-8 -*-
"""Multiprocessing-Comparison.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1adpP1NHW6kdM6DNPbUfseQBPQz8h33IS

# Comparison between Python Default Processing & Multiprocessing
## Akif Islam
## 07 August 2023

# Simple Processing
"""

number_in_range = 10000

import multiprocessing as mp
import time
import math


results_a = []
results_b = []
results_c = []

def make_calculation_one(numbers):
    for number in numbers:
        results_a.append(math.sqrt(number**3))

def make_calculation_two(numbers):
    for number in numbers:
        results_b.append(math.sqrt(number**4))

def make_calculation_three(numbers):
    for number in numbers:
        results_c.append(math.sqrt(number**5))

"""# Multiprocessing"""

import multiprocessing as mp
import time
import math


results_a = []
results_b = []
results_c = []

def make_calculation_one(numbers):
    for number in numbers:
        results_a.append(math.sqrt(number**3))

def make_calculation_two(numbers):
    for number in numbers:
        results_b.append(math.sqrt(number**4))

def make_calculation_three(numbers):
    for number in numbers:
        results_c.append(math.sqrt(number**5))



if __name__=='__main__':

  required_time_in_simple = []
  required_time_in_multi = []
  applied_range = []

  i = 1

  for _ in range (1000):
    i*=2;
    if(i>(2**24)):
      break

    applied_range.append(i)
    number_list=list(range(i))

    # Simple Threading
    start = time.time()
    make_calculation_one(number_list)
    make_calculation_two(number_list)
    make_calculation_three(number_list)

    end = time.time()

    turnaround_simple = round(end-start,2)
    required_time_in_simple.append(turnaround_simple)

    print(f"Required time in Simple for {i} : ",turnaround_simple)

    # Multi Processing
    p1 = mp.Process(target=make_calculation_one, args=(number_list,))
    p2 = mp.Process(target=make_calculation_two, args=(number_list,))
    p3 = mp.Process(target=make_calculation_two, args=(number_list,))

    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    end = time.time()

    turnaround_multi=round(end-start,2)
    required_time_in_multi.append(turnaround_multi)

    print(f"Required time in Multi for {i}: ",turnaround_multi)

"""# Comparison of Default Processing & Multiprocessing"""

applied_range

required_time_in_simple

required_time_in_multi

len(applied_range)

"""# Plot without Multiprocessing"""

from matplotlib import markers
import matplotlib.pyplot as plt
plt.plot(applied_range,required_time_in_simple,color='red',marker='o')
plt.grid(visible=True)
plt.xlabel('Length of List (Numbers)')
plt.ylabel('Required Time')
plt.title('Without Multiprocessing')
plt.show()

"""# Plot with Multiprocessing"""

plt.plot(applied_range,required_time_in_multi,color='blue',marker='o')
plt.grid(visible=True)
plt.xlabel('Length of List (Numbers)')
plt.ylabel('Required Time (secs)')
plt.title('With Multiprocessing')
plt.show()

"""# Combined Plot"""

end_boundary = 24

from matplotlib import markers
import matplotlib.pyplot as plt


plt.plot(applied_range[0:end_boundary],required_time_in_simple[0:end_boundary],color='red')
plt.plot(applied_range[0:end_boundary],required_time_in_multi[0:end_boundary],color='blue')
plt.grid(visible=True)

plt.xlabel('Length of List (Numbers)')
plt.ylabel('Required Time')
plt.title('Without Multiprocessing')
plt.show()

"""# Conclusion

- Multiprocessing is very very faster for higher numbers of elements. Its 128x faster for 2^23 elements
"""