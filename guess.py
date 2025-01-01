import random
start = input('請決定開始的數值: ')
end = input('請決定結束的數值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)

g1 = start
g2 = end
n = 0

print('請猜', g1, '-', g2, ': ')
g = input( )
g = int(g)
while g > g2 or g < g1:
	print('不對喔，請猜', g1, '-', g2, ': ')
	g = input( )
	g = int(g)
n = n + 1
while g != r:
	if g > r:
		print('你猜的數字比答案大')
		g2 = g
		print('請猜', g1, '-', g2, ': ')
		g = input( )
		g = int(g)
		while g > g2:
			print('不對喔，請猜', g1, '-', g2, ': ')
			g = input( )
			g = int(g)
		n = n + 1
		
	elif g < r:
		print('你猜的數字比答案小')
		g1 = g
		print('請猜', g1, '-', g2, ': ')
		g = input( )
		g = int(g)
		while g < g1:
			print('不對喔，請猜', g1, '-', g2, ': ')
			g = input( )
			g = int(g)
		n = n + 1

print('終於猜對了，你猜了', n, '次')