import os, sys, time, random

h1 = "ค้อน"
p2 = "กระดาษ"
g3 = "กรรไกร"

all = [h1, p2, g3]
#banner
def banner():
	os.system('clear')
	print('''
█▀█ █▀█ █▀▀ █▄▀   █▀█ ▄▀█ █▀█ █▀▀ █▀█
█▀▄ █▄█ █▄▄ █░█   █▀▀ █▀█ █▀▀ ██▄ █▀▄

█▀▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
█▄▄ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█
''')

#show banner
banner()
s = input('   ---เริ่มเกมส์---\n{ใช่ หรือ ไม่} = ')
if s == 'ใช่':
	
	while True:
		print('-----------------------------------------')
		print('>>โอเค เริ่มเกม เป่ายิงฉุบ!!<<')
		time.sleep(1.50)
		print('[อ่าน] ให้เลือกระหว่าง ค้อน กระดาษ และ กรรไกร \n() ให้เลือกอย่างใดอย่างหนึ่ง\nค้อน คือ เลข 1\nกระดาษ เลข 2\nกรรไกร เลข 3\n-----------------------------------------')
		c = int(input('>>โปรดเลือกเลข = '))
		time.sleep(0.50)
		if c > 3:
			print(f'!!! ไม่พบเลข {c}')
		elif c == 1:
			print(f'*คุณเลือกเลข {c} หรือ {h1}')
			ran = random.choice(all)
			print(f'คู่ต่อสู้ของคุณตอบ {ran}')
			if ran == h1:
				print('>>>เสมอ!!')
				time.sleep(2)
			elif ran == p2:
				print('>>>คุณแพ้!!')
				time.sleep(2)
			elif ran == g3:
				print('>>>คุณชนะ!!!')
				time.sleep(2)
		elif c == 2:
			print(f'*คุณเลือกเลข {c} หรือ {p2}')
			ran = random.choice(all)
			print(f'คู่ต่อสู้ของคุณตอบ {ran}')
			if ran == g3:
				print('>>>คุณแพ้!!')
				time.sleep(2)
			elif ran == p2:
				print('>>>เสมอ!!')
				time.sleep(2)
			elif ran == h1:
				print('>>>คุณชนะ!!!')
				time.sleep(2)
		elif c == 3:
			print(f'*คุณเลือกเลข {c} หรือ {g3}')
			ran = random.choice(all)
			print(f'คู่ต่อสู้ของคุณตอบ {ran}')
			if ran == h1:
				print('>>>คุณแพ้!!')
				time.sleep(2)
			elif ran == p2:
				print ('>>>คุณชนะ!!!')
				time.sleep(2)
			elif ran == g3:
				print('>>>เสมอ')
				time.sleep(2)
else:
	print(':]')
	sys.exit()

#โดย Potter
