
# BMI判定(例外処理あり版)

while True:
    try:
        # break するまで繰り返す
        weight = float(input("体重(kg)"))
        height = float(input("身長(cm)"))
        height = height / 100 # メートルになおす
        bmi = weight / (height * height)
        break;
    except Exception as e:
        print("入力ミスがあります")

result = ""
if bmi < 18.5: result = "痩せ型"
elif bmi < 25: result = "標準"

print("BMI:",bmi)
print("判定:",result)
