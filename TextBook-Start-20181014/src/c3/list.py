
import random

list_test = [1,1,2,3,5,8,13,21,34]

sum_list = 0
for i in list_test:
    sum_list += i
    # print(i, "を足して、合計は",sum_list)

ave_sum = sum_list / len(list_test) # 平均 = 合計 / リストの個数
# print("平均は",ave_sum)
# print("合計はsum(list_test) = ",sum(list_test))


# 格言リスト
list_kakugen = [
    "能ある鷹は爪を隠す"
    ,"豚に真珠"
    ,"二兎を追う者は一兎をも得ず"
    ,"叩き続けなさい、さすれば開かれます"
]
list_kakugen.append("格言追加")
list_range = list_kakugen[0:3]
print(list_range)
del list_range[1]
print(list_range)

# ランダムに一つ選ぶ
for counter in list_kakugen:
    i = random.randint(0, len(list_kakugen)-1)
    # print(list_kakugen[i])
