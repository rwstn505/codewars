def order_weight(string):
    def weight(n):
        return sum(int(digit) for digit in n), n
    
    return ' '.join(sorted(string.split(), key=weight))

print(order_weight("103 123 4444 99 2000"))  # "2000 103 123 4444 99"
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))  # "11 11 2000 10003 22 123 1234000 44444444 9999"
print(order_weight(""))  # ""