def decimal_to_binary(num):
    if num == 0: return '0'

    binary = ''
    while num != 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary

print(decimal_to_binary(0))
print(decimal_to_binary(1))
print(decimal_to_binary(2))
print(decimal_to_binary(8))
print(decimal_to_binary(10))
print(decimal_to_binary(11))