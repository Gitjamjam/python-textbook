
# 入力を得て、インチをセンチに

per_inch = 2.54

# ユーザーから入力を得る
user = input("何センチ(cm)?")
print(str(type((user))) + str(user))
inch = float(user)
print(str(type((inch))) + str(inch))
# 計算
cm = inch * per_inch

print("{0}インチ = {1}センチ".format(inch,cm))
