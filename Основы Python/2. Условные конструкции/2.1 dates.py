month = input("Введите месяц рождения: ");
month = month.lower();
date = int(input("Введите день рождения: "));

if month == 'март':
  sign = 'овен' if (date >= 21) else 'рыбы'
elif month == 'апрель':
  sign = 'телец' if (date >= 21) else 'овен'
elif month == 'май':
  sign = 'близнецы' if (date >= 22) else 'телец'
elif month == 'июнь':
  sign = 'рак' if (date >= 22) else 'близнецы'
elif month == 'июль':
  sign = 'лев' if (date >= 23) else 'рак'
elif month == 'август':
  sign = 'дева' if (date >= 24) else 'лев'
elif month == 'сентябрь':
  sign = 'весы' if (date >= 24) else 'дева'
elif month == 'октябрь':
  sign = 'скорпион' if (date >= 24) else 'весы'
elif month == 'ноябрь':
  sign = 'стрелец' if (date >= 23) else 'скорпион'
elif month == 'декабрь':
  sign = 'козерог' if (date >= 23) else 'стрелец'
elif month == 'январь':
  sign = 'водолей' if (date >= 21) else 'козерог'
elif month == 'февраль':
  sign = 'рыбы' if (date >= 21) else 'водолей'
print ("Ваш знак зодиака - " + sign);
