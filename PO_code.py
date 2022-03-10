
weight_p = float(input("Ввведите значение рассчетной нагрузки в кг/см2: "))
a = float(input("Ввведите значение длины (a) люка в мм: "))
b = float(input("Ввведите значение ширины (b) люка в мм: "))
h = float(input("Ввведите значение высоты  балки (h) в мм: "))
# h_k = float(input("Ввведите значение высоты пояса балки (hп) в мм: "))
number_n = int(input("Задайте количество балок: "))

weight_p_convert = weight_p * 0.01


number = number_n
result_lst = [x for x in range(1, number + 1)]  # формирую список из данных введенных пользователем
result_lst_int = []
for i in result_lst:
    result_lst_int.append(int(i))  # делаю список списком int

first_and_last_beams = [result_lst_int[0], result_lst_int[-1]]  # выношу в отдельный список первое и последнее значение
# print(first_and_last_beams)

all_beams = result_lst_int[1:][:-1]  # выношу в отдельный список оставшиеся значения (балки кроме 1й и крайней)
# print(all_beams)

calculation_d = b / (number - 1)  # Определили длину участка d
f_1 = str(round(calculation_d, 1))
# print("Длина участка (d) равна: " + f_1 + " [мм]")

calculation_f = weight_p_convert * (b * calculation_d)  # Подсчитали силу в клетке F
f_2 = str(round(calculation_f, 1))
# print("Сила в клетке (F) равна: " + f_2 + " [Н]")
calculation_perimeter = 2 * (b + calculation_d)  # Определили периметр прямоугольного сектора
f_3 = str(round(calculation_perimeter, 1))
# print("Периметр прямоугольного сектора равен: " + f_3)

print()
print()

for y in first_and_last_beams:
    if y == first_and_last_beams[0]:
        calculation_q_first = (calculation_f / calculation_perimeter)  # q
        m_max_first = (calculation_q_first * b**2) / 8  # Mmax
        strength_in_first_belt = (m_max_first / h)   # P - усилие в поясе
        square_first_belt = strength_in_first_belt / 40  # F площадь пояса
        volume_first_belt = square_first_belt * b  # V объем пояса
        weight_first_belt = 0.000027 * volume_first_belt  # 2.7 - плотность; масса пояса
        f_13 = str(round(weight_first_belt, 3))

        print("Масса пояса первой и последней балки равна: " + f_13 + " [кг]")

        lateral_force_in_first_belt = (calculation_q_first * b) / 2  # Q - поперечная сила
        thickness_in_first_wall = (lateral_force_in_first_belt / (24 * h))  # Дельта - толщина стенки
        square_first_wall = thickness_in_first_wall * h  # F - площадь стенки
        volume_first_wall = square_first_wall * b  # V объем стенки
        weight_first_wall = 0.000027 * volume_first_wall  # 2.7 - плотность; масса стенки
        f_5 = str(round(weight_first_wall, 3))

        print("Масса стенки первой и последней балки равна: " + f_5 + " [кг]")

        weight_first_belt_2 = weight_first_belt * 2
        weight_first_beam = weight_first_belt_2 + weight_first_wall  # масса первой балки
        f_6 = str(round(weight_first_beam, 3))

        print("Масса первой и последней балки равна: " + f_6 + " [кг]")
        sum_weight_first_and_last_beam = weight_first_beam * 2
        f_15 = str(round(sum_weight_first_and_last_beam, 3))
        print("Суммарная масса первой и последней балки равна: " + f_15 + " [кг]")

        print()

    else:
        calculation_q_last = (calculation_f / calculation_perimeter)
        m_max_last = (calculation_q_last * b**2) / 8
        strength_in_last_belt = (m_max_last / h)
        square_last_belt = strength_in_last_belt / 40
        volume_last_belt = square_last_belt * b
        weight_last_belt = 0.000027 * volume_last_belt
        lateral_force_in_last_belt = (calculation_q_last * b) / 2
        thickness_in_last_wall = lateral_force_in_last_belt / (24 * h)
        square_last_wall = thickness_in_last_wall * h
        volume_last_wall = square_last_wall * b
        weight_last_wall = 0.000027 * volume_last_wall
        weight_last_beam = (weight_last_belt * 2) + weight_last_wall


for z in all_beams:
    calculation_q_remaining = (calculation_f / calculation_perimeter) * 2
    m_max_remaining = (calculation_q_remaining * b**2) / 8
    strength_in_remaining_belt = (m_max_remaining / h)
    square_remaining_belt = strength_in_remaining_belt / 40
    volume_remaining_belt = square_remaining_belt * b
    weight_remaining_belt = 0.000027 * volume_remaining_belt
    f_15 = str(round(weight_remaining_belt, 3))
    print("Масса пояса центральной балки равна: " + f_15 + " [кг]")
    lateral_force_in_remaining_belt = (calculation_q_remaining * b) / 2
    thickness_in_remaining_wall = lateral_force_in_remaining_belt / (24 * h)
    square_remaining_wall = thickness_in_remaining_wall * h
    volume_remaining_wall = square_remaining_wall * b
    weight_remaining_wall = 0.000027 * volume_remaining_wall
    f_16 = str(round(weight_remaining_wall, 3))
    print("Масса стенки центральной балки равна: " + f_16 + " [кг]")
    weight_remaining_beams = ((weight_remaining_belt * 2) * len(all_beams)) + (weight_remaining_wall * len(all_beams))
    weight_solo_remaining_beams = weight_remaining_beams / len(all_beams)
    f_21 = str(round(weight_solo_remaining_beams, 3))
    print("Масса одной центральной балки равна: " + f_21 + " [кг]")
    f_9 = str(round(weight_remaining_beams, 3))
    print("Суммарная масса центральных балок равна: " + f_9 + " [кг]")

    print()


beam_mass = weight_first_beam + weight_last_beam + weight_remaining_beams


f_11 = str(round(beam_mass, 3))
print("Масса балок равна: " + f_11 + " [кг]")
k_1 = beam_mass / b
k_2 = k_1 * calculation_d
k_3 = number_n + 1
f_m = k_2 * k_3
f_m_r = round(f_m, 3)
# frame_mass = ((beam_mass / b) * calculation_d) * (calculation_d + 1)

f_12 = str(f_m_r)
print("Масса балок с рамой равна: " + f_12 + " [кг]")

mass_kr = 0.160 * 8
mass_ob = 0.750 + 0.340

all_mass = f_m + mass_kr + mass_ob + 1.1
f_14 = str(round(all_mass, 3))

print("Итоговая масса люка равна: " + f_14 + " [кг]")




