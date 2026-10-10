# write a program to find factorial of n(n is parameter)

def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

calc_fact(6)

# write a program to convert usd into inr

def converter(usd_val):
    inr_value = usd_val * 95
    print(usd_val, "USD = ", inr_value, "INR")

converter(3)