
# 数値と文字の結合
kion_1 = 30
kion = str(kion_1)
print("今日の気温は", kion, "度です")


# formatで値を埋め込む
per_inch = 2.54
inch = 24
cm = inch * per_inch
# 文字列で説明を加える
desc = "{0}インチ = {1}センチ".format(inch,cm)
print(desc)
print("私は{name}です。".format(name="なまえ"))

fmt = "年齢は{age}歳で、{job}をやっています"
str_fmt = fmt.format(age=22, job="なまえ")
print(str_fmt)