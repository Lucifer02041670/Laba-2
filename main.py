Color1_ = input("Введите первый цвет:\n")
Color2_ = input("Введите второй цвет:\n")

if (Color1_ == "Красный" or Color1_ == "красный") and (Color2_ == "Синий" or Color2_ == "синий"):
    print("Фиолетовый")
elif (Color1_ == "Красный" or Color1_ == "красный") and (Color2_ == "Желтый" or Color2_ == "желтый"):
    print("Оранжевый")
elif (Color1_ == "Синий" or Color1_ == "Синий") and (Color2_ == "Желтый" or Color2_ == "Желтый"):
    print("Зеленый")
else:
    print("ОШИБКА! \nВведен неверный цвет!")