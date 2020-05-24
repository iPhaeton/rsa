def decimal_to_binary(num):
    if num == 0: return '0'

    binary = ''
    while num != 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary

def modulo(numerator, exp, denominator):
    binary = decimal_to_binary(exp)
    powers = set()

    for i, reg in enumerate(binary[::-1]):
        if (reg == '1'):
            powers.add(pow(2, i))

    prev_result = numerator
    result = 1
    for i in range(1, len(binary)):
        prev_result = (prev_result * prev_result) % denominator
        if pow(2, i) in powers:
            result *= prev_result
        
    if 1 in powers:
        result *= numerator
    
    return result % denominator

print(modulo(5, 149, 17))

# print(decimal_to_binary(0))
# print(decimal_to_binary(1))
# print(decimal_to_binary(2))
# print(decimal_to_binary(8))
# print(decimal_to_binary(10))
# print(decimal_to_binary(11))