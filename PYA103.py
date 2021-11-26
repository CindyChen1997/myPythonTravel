# TODO
# 請撰寫一程式，輸入四個單字，然後將這四個單字以欄寬為10、欄與欄間隔一個空白字元、每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。
ph1=input()
ph2=input()
ph3=input()
ph4=input()

# 靠右對齊
# TODO
print('|{0:>10s} {1:>10s}|'.format(ph1,ph2))
print('|{0:>10s} {1:>10s}|'.format(ph3,ph4))
# 靠左對齊
print('|{0:10s} {1:10s}|'.format(ph1,ph2))
print('|{0:10s} {1:10s}|'.format(ph3,ph4))
# TODO
