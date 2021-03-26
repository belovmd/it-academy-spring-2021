rubles, penny = (
    int(input('Введите количество рублей: ')),
    int(input('Введите количество копеек: ')))
total = (rubles * 100 + penny) * 3
rubles = total // 100
penny = total % 100
tenths_r = rubles % 10
hundredths_r = rubles % 100
tenths_p = penny % 10
hundredths_p = penny % 100
if tenths_r == 1 and hundredths_r != 11:
    ending_rubles = 'ь'
elif 1 < tenths_r < 5 and not 11 < hundredths_r < 15:
    ending_rubles = 'я'
else:
    ending_rubles = 'ей'
if tenths_p == 1 and hundredths_p != 11:
    ending_penny = 'йка'
elif 1 < tenths_p < 5 and not 11 < hundredths_p < 15:
    ending_penny = 'йки'
else:
    ending_penny = 'ек'
print('Общая цена: ', rubles, 'рубл' + ending_rubles, penny, 'копе' + ending_penny)
