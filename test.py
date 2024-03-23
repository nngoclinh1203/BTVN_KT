def calculate_bmi(weight, height):
    bmi = 0.0
    bmi = weight / (height ** 2)
    bmi = round(bmi, 1)
    if bmi < 18.5:
        return "Thiếu cân"
    elif bmi < 23:
        return "Bình thường"
    elif bmi < 25:
        return "Thừa cân"
    else:
        return "Béo phì"

weight = float(input("Nhập cân nặng của bạn (kg): "))
height = float(input("Nhập chiều cao của bạn (m): "))

print(calculate_bmi(weight, height))
