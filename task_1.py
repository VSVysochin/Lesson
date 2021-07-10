enter_second = int(input("Введите количество секунд: "))

days = enter_second // 3600 // 24
hours = enter_second // 3600 - days * 24
minutes = enter_second // 60 % 60
second = enter_second % 60

print("В", int(enter_second), "секундах:", int(days), "дня,", int(hours), "часов,", int(minutes), "минут,", int(second),"секунд")
