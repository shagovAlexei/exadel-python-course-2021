# Shagov Aleksei
# Function to count digit in number
def count_tens(n):
    count = 0
    while n:
        n //= 10
        count += 1
    return count


# Returns true if n is Narcissistic number
def is_narcissistic_number(n):
    number_copy = n
    arm_sum = 0
    digit = count_tens(n)
    while n:
        remainder = n%10
        arm_sum += remainder**digit
        n //= 10
    return arm_sum == number_copy

# Loop
for i in range(1,1000):
    if is_narcissistic_number(i):
        print(i, end=' ')
