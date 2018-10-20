
# BMI判定プログラム
height = float(input("身長(cm)は："))
weight = float(input("体重(kg)は："))
# BMIの計算
height = height / 100 # mに直す
bmi = weight / (height * height)
result = "" # resultの初期化

if bmi < 18.5:
    result = "痩せ型"
if bmi >= 18.5 and bmi < 25:
    result = "標準"
if bmi >= 25 and bmi < 30:
    result = "肥満(軽)"
if bmi >= 30:
    result = "肥満(重)"

# 結果を表示
print("BMI = ", bmi)
print("判定 ... ",result)