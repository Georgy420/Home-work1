time = int(input("Введите время в секундах: "))

hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)

print (f"Время в формате: {hours} часов, {minutes} минут, {seconds} секунд")