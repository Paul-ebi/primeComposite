#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import random


# In[2]:


def simple_prime(n):
    if n < 2:
        return False, 0
    iterations = 0
    for i in range(2, n):
        iterations += 1
        if n % i == 0:
            return False, iterations
    return True, iterations


# In[3]:


def miller_prime(n):
    if n < 2:
        return False, 0
    if n == 2 or n == 3:
        return True, 0
    if n % 2 == 0 or n % 3 == 0:
        return False, 0
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    iterations = 0
    k = 10
    for i in range(k):
        a = random.randint(2, n-2)
        x = pow(a, d, n)
        iterations += 1
        if x == 1 or x == n-1:
            continue
        for j in range(s-1):
            x = pow(x, 2, n)
            iterations += 1
            if x == n-1:
                break
        else:
            return False, iterations
    return True, iterations


# In[4]:


def get_factors(n):
    factors = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors


# In[5]:


def main():
    num = int(input("Enter a number: "))
    #method = int(input("Which method would you like to use? (1 or 2): "))
    #if method == 1:
    is_prime_simple, iterations_simple = simple_prime(num)
    #elif method == 2:
    is_prime_miller, iterations_miller = miller_prime(num)
    #else:
        #print("Invalid method selected.")
        #return

    if is_prime_simple:
        print(f"{num} is a prime number (Simple Prime).")
    else:
        print(f"{num} is a composite number (Simple Prime).")
        factors = get_factors(num)
        print(f"The factors of {num} are: {factors}")
    print(f"Number of iterations (Simple Prime): {iterations_simple}")

    if is_prime_miller:
        print(f"{num} is a prime number (Miller Prime).")
    else:
        print(f"{num} is a composite number (Miller Prime).")
        factors = get_factors(num)
        print(f"The factors of {num} are: {factors}")
    print(f"Number of iterations (Miller Prime): {iterations_miller}")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




