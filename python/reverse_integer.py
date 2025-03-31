def reverse_integer(n):
    reversed_num = int(str(abs(n))[::-1])
    return -reversed_num if n < 0 else reversed_num

print(reverse_integer(500))
print(reverse_integer(-56))
