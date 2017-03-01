# -*- coding:utf-8 -*-

#汉诺塔的代码实现，其实就是练习递归的使用方法
#参考资料http://baike.baidu.com/item/%E6%B1%89%E8%AF%BA%E5%A1%94/3468295

def move(n, a, b, c):
	if n == 1:
		print(a,'-->', c) #如果只有一个，则直接从a->c
	else:
		move(n-1, a, c, b) #先把n-1个盘子丢到c上
		move(1, a, b, c)   #然后把最后一个大盘子丢到b上
		move(n-1, b, a, c) #最后将原来移动到b的盘子移动到c

#测试
print(move(3, 'A', 'B', 'C'))