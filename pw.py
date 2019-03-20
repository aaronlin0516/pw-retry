password = 'a123456'
i=3
while True:
	s1 = input('請輸入密碼: ')
	if s1 == password:
		print('登入成功!')
		break #成功之後離開迴圈
	else:
		i = i -1
		print('密碼錯誤! 還有', i, '次機會')
		if i == 0:
			break