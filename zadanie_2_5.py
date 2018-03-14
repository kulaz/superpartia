rok = int(input('Podaj rok: '))
mies = 0
while mies <= 0 or mies > 12:
    mies = int(input('Podaj numer miesiąca (np. styczeń - 1): '))
    if mies <= 0 or mies > 12:
        print('Podaj prawidłowy miesiąc w przedziale 1 do 12')
dzien = 0
while dzien <= 0 or dzien > 31:
    dzien = int(input('Podaj dzień: '))
    if dzien <= 0 or dzien > 31:
        print('Podaj prawidłowy dzień: ')
print('Obliczam dla: ' + 'rok ' + str(rok) +', ' + 'miesiąc ' \
      + str(mies) + ', ' + 'dzień ' + str(dzien) + '.')

mies -= 2
if mies <= 0:
    mies+=12
    rok-=1
wynik = mies * 83 // 32
wynik+=dzien
wynik+=rok
rok1 = rok // 4
wynik+=rok1
rok2 = rok // 100
wynik-=rok2
rok3 = rok // 400
wynik += rok3
wynik = wynik % 7
if wynik == 0:
    print('Niedziela!')
elif wynik == 1:
    print('Poniedziałek!')
elif wynik == 2:
    print('Wtorek!')
elif wynik == 3:
    print ('Środa!')
elif wynik == 4:
    print('Czwartek')
elif wynik == 5:
    print('Piątek')
else:
    print('Sobota')

