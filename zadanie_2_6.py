h=-1
while h < 0 or h > 23:
    h = int(input('Podaj godzinę: '))
    if h < 0 or h > 23:
        print('Podaj liczbę w przedziale 0 - 23')
m=-1
while m < 0 or m > 59:
    m = int(input('Podaj minutę: '))
    if m < 0 or m > 59:
        print('Podaj liczbę w przedziale 0 - 59')

plus=-1
while plus < 0 or plus > 43200:
    plus = int(input('Chcesz sprawdzić godzinę, która będzie za ... minut: '))
    if plus < 0 or plus > 43200:
        print('Podaj liczbę w przedziale 0 - 43200')

h1 = h*60
wynik = h1 + m + plus
h2=wynik//60
m2=wynik%60

if h2 >=24:
    h2=h2%24
print((str(h2)) + ':' + (str(m2)))

