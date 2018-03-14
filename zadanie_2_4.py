c = int(input('Podaj liczbę: '))
while True:
    if c % 2 == 0:
        c /= 2
        print(c)
    else:
        c = 3 * c +1
        print(c)
    if c == 1:
        break
    else:
        continue
print('Lothar Collatz miał rację!')
    
    
        


