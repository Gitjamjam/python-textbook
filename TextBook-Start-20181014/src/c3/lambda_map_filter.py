
# リストを作成
nums = [1, 3, 5, 7, 9]

# 値を2倍にする無名関数
x2 = lambda x:x*2
# mapを使ってリストnumsにx2を適用
print(list(map(x2,nums)))

nums = [1,2,3,11,12,13,21,22,23]
# 奇数のものを抽出
print(list(filter(lambda x:(x%2) == 1, nums)))
