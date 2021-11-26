#TODO
#請撰寫一程式，輸入四個整數，然後將這四個整數以欄寬為5、欄與欄間隔一個空白字元，再以每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。

num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())

#向右靠齊
#TODO
print('|{0:5d} {1:5d}|'.format(num1,num2))
print('|{0:5d} {1:5d}|'.format(num3,num4))

#向左靠齊
print('|{0:<5d} {1:<5d}|'.format(num1,num2))
print('|{0:<5d} {1:<5d}|'.format(num3,num4))
#TODO
