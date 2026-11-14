DAILY_WATER_ML_PER_KG = 30
ML_PER_LITER = 1000


# Сохраняем имя
user_name = input('Как вас зовут?')
# Сохраняем возраст
try:
    user_age = int(input('Сколько вам лет?'))
except ValueError:
    print('Ошибка! Укажите ваш возраст числовым значением')
# Сохраняем вес
try:
    user_weight = float(input('Укажите ваш вес в кг'))
except ValueError:
    print('Ошибка! Укажите ваш вес числовым значением')

# Сохраняем рост в метрах
try:
    user_height = float(input('Укажите ваш рост в метрах (Например 1.75)'))
except ValueError:
    print("Ошибка! Введите только число.")

# Вычисляем BMI по формуле - вес деленный на рост возведенный в квадрат
bmi = round(user_weight / (user_height ** 2), 1)
# Расчитываем норму воды в литрах в день
water_needed_in_liters = (user_weight * DAILY_WATER_ML_PER_KG) / ML_PER_LITER
# Выводим красивую печать в терминале
print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_needed_in_liters:.1f} л. в день')
print()
print('Расчет окончен. Будьте здоровы!')
