def decimal_to_binary(num):
    if num == 0: return '0'

    binary = ''
    while num != 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary

def modulo(numerator, exp, denominator):
    binary = decimal_to_binary(exp)

    prev_result = numerator
    result = 1
    for i in range(len(binary) - 2, -1, -1):
        reg = binary[i]
        prev_result = (prev_result * prev_result) % denominator
        if (reg == '1'):
            result *= prev_result
        
    if binary[0] == '1':
        result *= numerator
    
    return result % denominator

# print(modulo(5, 149, 17))

# print(decimal_to_binary(0))
# print(decimal_to_binary(1))
# print(decimal_to_binary(2))
# print(decimal_to_binary(8))
# print(decimal_to_binary(10))
# print(decimal_to_binary(11))