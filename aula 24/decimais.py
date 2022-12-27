import decimal

a, b = 0.2, 0.1
c, d = decimal.Decimal('0.1'), decimal.Decimal('0.2')

print(a + b)

print(round((a + b), 2)) # não exibe os zeros no final 
print(c + d)
