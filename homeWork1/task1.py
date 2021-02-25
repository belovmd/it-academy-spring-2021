M = int(input('Стоимость (рублей)'))
N = int(input('Стоимость (копеек)'))
S = int(input('Количество товара'))

COST_R = S*M + N*S // 100
COST_C = N*S % 100

print(COST_R, '.', COST_C)
