# Shagov Aleksei
# Function to count digit in number
def count_digit(n):
    count = 0
    while n:
        n //= 10
        count += 1
    return count


# Returns true if n is Narcissistic number
def check(n):

    if n < 0:
        return False
    
    number_copy = n
    arm_sum = 0
    digit = count_digit(n)
    while n:
        remainder = n%10
        arm_sum += remainder**digit
        n //= 10

    return arm_sum == number_copy

# Loop
for i in range(1,1000):
    if check(i):
        print(i, end=' ')
