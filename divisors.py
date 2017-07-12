#printout all divisors

user_input = int(input(" Enter number to return list of divisors"))
divisors = []
for i in range(1, user_input):
    if user_input % i == 0:
        divisors.append(i)
print(divisors)