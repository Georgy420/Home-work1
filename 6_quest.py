a = float(input("Введите результат пробежки первого дня в км.: "))
b = float(input("Введите общий желаемый результат в км.: "))
result_days = 1
result_km = a
while result_km < b:
    a = a + 0.1 * a
    result_days += 1
    result_km = result_km + a
print(f"Если продолжите в том же духе, то вы достигните нужных результатов на %.d день" % result_days)