
#カラットからグラムに変化する
#変換の元になる値
per_ct = 0.2
# ユーザーから入力
user = input("何カラットですか?")
ct = float(user)
# 計算する
g = ct * per_ct
# 結果を表示
print("{0}カラット(ct) = {1}グラム(g)".format(ct,g))
