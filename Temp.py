print("===== TEMPERATURE CONVERTER =====")
print("1. Celcius to Farenheit")
print("2. Farenheit to Celcius")
print("3. Kelvin to Celcius")
print("===============================")

choice = int(input("Enter your choice: "))

if choice == 1:
    c = float(input("Enter Celcius: "))
    f = (c * 9 / 5) + 32
    print("Result :")
    print(c, "C =", f, "F")

elif choice == 2:
    f = float(input("Enter Farenheit: "))
    c = (f - 32) * 5 / 9
    print("Result :")
    print(f, "F =", round(c), "C")

elif choice == 3:
    k = float(input("Enter Kelvin: "))
    c = k - 273.15
    print("Result :")
    print(k, "K =", round(c, 2), "C")

else:
    print("Choice is wrong")
