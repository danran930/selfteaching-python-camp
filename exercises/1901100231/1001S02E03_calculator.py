#告知这是个计算机小程序
a="1"

print("""请键入要进行运算的两个数字
 并按:
 “+”代表加
 “-”代表减
 “*”代表乘
 “/”代表除
 “%”代表求余数
 “**”代表求次方
 的如上所示的规则键入你要进行的运算
 本程序可多次使用，重复上述过程即可
 请切换至英文输入模式进行数字和运算的键入""")
 #获取要算的数和运算
while a=="1":
 x = input("请输入第一个数字")
 y = input("请输入第二个数字")
 z = input("请输入要进行的运算类型")
#计算器程序
 if z == "+":
   print(x,"+",y,"=",int(x)+int(y))#加法
 elif z== "-":
   print(x,"-",y,"=",int(x)-int(y))#减法   
 elif z== "*":
    print(x,"*",y,"=",int(x)*int(y))#乘法
 elif z== "/":
    print(x,"/",y,"=",int(x)/int(y))#除法
 elif z== "%":
    print(x,"除以",y,"的余数是",int(x)%int(y))#余数 
 elif z== "**":
    print(x,"的",y,"次方是",int(x)**int(y))#次方             





    
