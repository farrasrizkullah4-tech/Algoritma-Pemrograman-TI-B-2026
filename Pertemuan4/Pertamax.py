try:
    jarak = float(input("Jarak perjalanan (km): "))
    bensin = float(input("Bensin yang digunakan (liter): "))

    if jarak <= 0:
        print("Jarak harus lebih dari 0")
    elif bensin <= 0:
        print("Bensin harus lebih dari 0")
    else:
        konsumsi = jarak / bensin
        print("Konsumsi BBM:", konsumsi, "km/liter")

except ValueError:
    print("Input harus angka")