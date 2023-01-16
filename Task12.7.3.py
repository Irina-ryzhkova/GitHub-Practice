per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Сумма депозита: "))
Deposit = {}
for b,c in per_cent.items():
    Deposit[b] = round(c * money/100,2)
Deposit = {b: c for b, c in Deposit.items() if c == max(Deposit.values())}
for key, value in Deposit.items():
    print("Самая большая процентная ставка по вашему депозиту в банке ", key,)
    print("Сумма дохода в этом банке составит: ", value, " рублей!")