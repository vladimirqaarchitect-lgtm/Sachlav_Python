# try:
#     result = 10 / 0
#     print(result)
# except ZeroDivisionError:
#     print("Ошибка: Нельзя делить на ноль!")
#
# print("Программа продолжает работу после обработки ошибки.")
#
# # Пример 2: Несколько исключений
#
# try:
#     # num = int("abc") # Это вызовет ValueError
#     my_list = [1, 2]
#     print(my_list[3]) # Это вызовет IndexError
# except ValueError:
#     print("Ошибка преобразования типа данных!")
# except IndexError:
#     print("Ошибка: Индекс выходит за границы списка!")
# except Exception as e: # Общий обработчик для всех остальных исключений
#     print(f"Произошла непредвиденная ошибка: {e}")

# def divide_numbers(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         print("Нельзя делить на ноль!")
#         return None
#     else:
#         print(f"Деление успешно выполнено. Результат: {result}")
#         return result
#     finally:
#         print("Этот блок выполняется всегда (finally).")
#
# print("\n--- Первый вызов (без ошибки) ---")
# divide_numbers(10, 2)
#
# print("\n--- Второй вызов (с ошибкой) ---")
# divide_numbers(10, 0)

# Закрытие файлов (САМЫЙ частый случай)
# try:
#     file = open("data.txt")
#     data = file.read()
#     print(data)
# except FileNotFoundError:
#     print("Файл не найден")
# finally:
#     file.close()
#     print("Файл закрыт")

# Закрытие соединений (БД, API, сокеты)
# connection = None
# try:
#     connection = "Соединение с БД"
#     print("Работаем с базой данных")
#     raise Exception("Ошибка запроса")
# except Exception as e:
#     print("Ошибка:", e)
# finally:
#     if connection:
#         print("Соединение закрыто")


# 3. Освобождение ресурсов (память, устройства)
# try:
#     print("Открываем камеру")
#     raise RuntimeError("Камера недоступна")
# except RuntimeError as e:
#     print(e)
# finally:
#     print("Освобождаем камеру")

# 4. Логирование (запись факта выполнения)

# try:
#     print("Начало операции")
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Ошибка деления")
# finally:
#     print("Операция завершена (записано в лог)")

# 5. Очистка временных данных

# temp_data = []
# try:
#     temp_data.append("данные")
#     raise Exception("Ошибка")
# except Exception:
#     print("Ошибка обработки")
# finally:
#     temp_data.clear()
#     print("Временные данные очищены")

# 6. Почему finally, если есть return?
#
# def example():
#     try:
#         return "Результат"
#     finally:
#         print("finally выполнен")
#
# example()


# def check_age(age):
#     if not isinstance(age, (int, float)):
#         raise TypeError("Возраст должен быть числом.")
#     if age < 0:
#         raise ValueError("Возраст не может быть отрицательным.")
#     if age < 18:
#         print("Вам меньше 18 лет.")
#     else:
#         print("Вам 18 лет или больше.")
#
# try:
#     check_age(25)
#     check_age(-5) # Это вызовет ValueError
# except (TypeError, ValueError) as e:
#     print(f"Ошибка при проверке возраста: {e}")
#
# try:
#     check_age("десять") # Это вызовет TypeError
# except (TypeError, ValueError) as e:
#     print(f"Ошибка при проверке возраста: {e}")

# def withdraw(balance, amount):
#     if amount > balance:
#         raise ValueError("Недостаточно средств")
#     return balance - amount
#
# try:
#     withdraw(100, 200)
# except ValueError as e:
#     print("Показываем сообщение клиенту:", e)
