# 数据类型
# 整型
intvar = 10
# 浮点型
floatvar = 1.234
# 布尔类
boolvar = True

# 函数转换
# print(bool(floatvar))
#表示0，None，空的量（None)代表假（False)
# 1代表真（True）非空的量（字符串等类型），非零的数值（数值类型）

# 序列
# 数据结构
# 有序序列
# 字符串
# strvar = 'admin'
# 查[]加的是下标（索引）
# print(strvar[3])
# print(strvar.find('a'))

# 字符串是不可以修改的
# strvar2 = (strvar[1])

# 替换
# print('修改前的字符串是',strvar)
# strvar3 = (strvar.replace('min','nibaba'))
# print('修改后的字符串是',strvar)
# print('新生成的字符串是',strvar3)

# 把字符串变成列表（分隔字符串）
# strvar4 = 'hello@163.com'
# strvar5 = 'a,b,c,d,e'
# print(strvar4.split('@'))
# print(strvar5.split(','))

# format()格式化字符串
# strvar6 = 'admin'
# intvar = 10
# floatvar = 3.14
# listvar = [10,39]
# print('测试报告{}..///{}{}'.format(listvar,floatvar,listvar))

# 列表
listvar = ['admin',10,3.14,[10, ],(231,322225)]
# 列表里面有单个数值的时候不需要加,
listvar2 = [10,2030,394]

# 列表增加一个值
# print('原来的列表里面有',listvar2)
# listvar2.append(80)
# print('增加后的列表里面有',listvar2)
# listvar2.insert(1,234325)
# print('使用下标增加后的列表里面有',listvar2)

# 列表删除一个值
# listvar2.pop()
# print('删除后',listvar2)
# listvar2.pop(0)
# print('使用下标删除',listvar2)

# 查询列表10所在的位置
# 下标的位置是从0开始的
# 0=10, 1=2030 2=394
# print('列表10所在的位置是',listvar2.index(10))
listvar3 = [10,20,30,40,50,60,70,80]

# 查询到列表里面的值
# print(listvar3[1])
# 1代表起始位置 4 最终位置（欺骗+1) 1 步长
# print(listvar3[1:4:1])
# print(listvar3[1:4:2])
# print(listvar3[1:4:3])

# 修改
# print('修改前数据是',listvar3)
# listvar3[2] = 'dusgiudgs'
# print('修改后数据是',listvar3)

