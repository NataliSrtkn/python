
#Вам дан словарь per_cent с распределением процентных ставок по вкладам в различных банках таким образом,
# что ключ — название банка, значение — процент.
# Напишите программу, в результате которой будет сформирован список deposit значений —
# накопленные средства за год вклада в каждом из банков.
# На вход программы с клавиатуры вводится сумма money, которую человек планирует положить под проценты.

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('Введите сумму,  которую  запланировали положить под проценты: '))
# создать пустой список
deposit = []

for i in per_cent:
    #print(i, per_cent[i])
    # добавить в пустой список произведение money на per_cent
    deposit.append(round(money * per_cent[i]/100, 2))
# распечатать получившийся список
print(f'Сумма процентов к выплате в каждом из банков\n{deposit}')
print()
# получить список банков и сделать из него список
bank = list(per_cent.keys())
print(f'Максимальная сумма, которую вы можете заработать - {max(deposit)} в банке {bank[deposit.index(max(deposit))]}')

