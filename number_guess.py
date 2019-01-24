#猜數字遊戲
upper_limit = int(input('請決定猜數字的範圍要從1到哪個整數(N)呢?'))
import random
answer = random.randint(1,upper_limit)
n = 0
while n < 5:
	m = 4 - n
	s = n + 1
	keyin = int(input('請從1到N之中猜一個數字(整數)'))
	if m == 0:
		print('很抱歉! 遊戲結束了!')
		break
	elif keyin == answer:
		print('答對了!!')
		print('你總共猜了', s, '次')
		break
	else:
		print('猜錯了, 再猜一次吧!')
		if keyin > answer:
			print('提示:你輸入的數字比答案大')
		elif keyin < answer:
			print('提示:你輸入的數字比答案小')
		print('剩餘次數 = ', m, '次')
	n = n + 1
print('正確答案是: ', answer)

