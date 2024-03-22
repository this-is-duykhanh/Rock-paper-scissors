try:
	import pygame
	import time
	from random import randint
	from datetime import datetime,date

	WIDTH_HOLD = 22
	HEIGHT_HOLD = 12
	GREY = (150,150,150)
	WHITE = (255,255,255)
	BLACK = (0,0,0)
	RED  = (255,0,0)
	ORANGE = (255,165,0)
	BACK_GROUND_GAME = (204, 229, 255)
	RED_WHITE = (255,51,51)
	BLUE = (0,128,255)

	WIDTH = 1100
	HEIGHT = 600
	
	size_hold = WIDTH/WIDTH_HOLD

	pygame.init()
	# tạo màn hình
	screen = pygame.display.set_mode((WIDTH,HEIGHT))

	pygame.display.set_caption("Scissors Rock Paper")

	font_head = pygame.font.SysFont('sans',80)
	font_text = pygame.font.SysFont('sans',40)
	font_name = pygame.font.SysFont('sans',30)
	font_38 = pygame.font.SysFont('sans',38)
	font_time = pygame.font.SysFont('sans',25)

	text_7 = font_name.render('YOU',True,BLACK)
	text_8 = font_name.render('COMPUTER',True,BLACK)
	text_9 = font_name.render('RESET',True,BLACK)
	text_10 = font_name.render('mic',True,BLACK)
	text_12 = font_text.render('-',True,WHITE)
	text_13 = font_text.render('+',True,WHITE)

	text_victory = font_head.render('VICTORY',True,BLUE)
	text_gameover = font_head.render('GAME OVER',True,BLUE) 
	text_continue = font_name.render('continue',True,WHITE) 
	text_exit = font_name.render('exit',True,WHITE)
	text_qestion_continue = font_name.render('DO YOU WANT TO PLAY AGAIN?',True,WHITE)

	# tải hình ành
	keo_img = pygame.image.load("image/Keo.png")
	bua_img = pygame.image.load("image/Bua.png")
	Paper_img = pygame.image.load("image/Bao.png")

	img_player_result = None
	img_computer_result = None

	setUp = True
	start_game = True
	running = True
	start = False
	draw_img_choose = False
	player = ""
	result = "set point please"
	computer =""
	your_score = 0
	computer_score = 0
	set_point = 0
	width_img_choose = 4*size_hold
	height_img_choose = 3*size_hold
		
	clock = pygame.time.Clock()

	channel_0 = pygame.mixer.Channel(0)
	channel_1 = pygame.mixer.Channel(1)
	channel_2 = pygame.mixer.Channel(2)


	sound_open_game = pygame.mixer.Sound("sound/game.mp3")
	sound_click = pygame.mixer.Sound("sound/click_mouse.mp3")
	sound_open_game.set_volume(0.1)

	sound_modification = pygame.mixer.Sound("sound/click.wav")
	sound_game = False
	sound_lose = pygame.mixer.Sound("sound/lose.wav")
	sound_win = pygame.mixer.Sound("sound/answer_right.mp3")

	sound_lose_game = pygame.mixer.Sound("sound/falling_game_over.wav")
	sound_win_game = pygame.mixer.Sound("sound/Am-thanh-chien-thang-www_tiengdong_com.mp3")

	def reset(your_score, computer_score, player, draw_img_choose, setUp, result):
		your_score = 0
		computer_score = 0
		player = ""
		img_player_result = ""
		img_computer_result = ""
		result = "set point please"
		setUp = True
		draw_img_choose = False
		return your_score, computer_score, player, draw_img_choose, setUp, result

	while running:
		clock.tick(90)
		# tạo màu nền
		
		# vị trí chuột
		mouse_x, mouse_y = pygame.mouse.get_pos()
		screen.fill(BACK_GROUND_GAME)
		#vẽ thiết kế
		if start_game:

			if player == "Scissors":
				pygame.draw.rect(screen, RED,(size_hold -2, size_hold*3 - 2, size_hold*2+4, size_hold+4))
			elif player == "Rock":
				pygame.draw.rect(screen, RED,(size_hold -2, 4.5*size_hold - 2, size_hold*2 + 4, size_hold + 4))
			elif player == "Paper":
				pygame.draw.rect(screen, RED,(size_hold -2, size_hold*6 -2, size_hold*2 +4 , size_hold + 4))

			pygame.draw.rect(screen, WHITE,(size_hold*4, size_hold, size_hold*3, size_hold))
			pygame.draw.rect(screen, WHITE,(size_hold*15, size_hold, size_hold*3, size_hold))
			pygame.draw.rect(screen, WHITE,(8*size_hold, 3*size_hold, 6*size_hold, 3*size_hold))
			pygame.draw.rect(screen,BLACK,(8*size_hold -1, 8*size_hold, 6*size_hold + 2, size_hold))
			pygame.draw.rect(screen,WHITE,(9*size_hold , 8*size_hold + 1, 4*size_hold, size_hold - 1))
			pygame.draw.rect(screen,BLACK,(5*size_hold - 1, 9*size_hold, 12*size_hold + 2, size_hold*2))

			# l là độ dài của thanh điểm
			l = 4*size_hold - 1
			pygame.draw.rect(screen, WHITE,(5*size_hold, 9*size_hold + 1, 4*size_hold - 1, 2*size_hold - 2))
			if your_score > 0:
				pygame.draw.rect(screen, RED,(5*size_hold, 9*size_hold + 1, your_score*l/set_point, 2*size_hold - 2))

			pygame.draw.rect(screen, WHITE,(9*size_hold, 9*size_hold + 1, 4*size_hold, 2*size_hold - 2))

			pygame.draw.rect(screen, WHITE,(13*size_hold + 1, 9*size_hold + 1, 4*size_hold - 1, 2*size_hold - 2))
			if computer_score > 0:
				pygame.draw.rect(screen, RED,(13*size_hold + 1, 9*size_hold + 1, computer_score*l/set_point, 2*size_hold - 2))


			screen.blit( pygame.transform.scale(keo_img, (2*size_hold, 1*size_hold)), (size_hold, size_hold*3, size_hold*2, size_hold))
			screen.blit( pygame.transform.scale(bua_img, (2*size_hold, 1*size_hold)), (size_hold, size_hold*4.5, size_hold*2, size_hold))
			screen.blit( pygame.transform.scale(Paper_img, (2*size_hold, 1*size_hold)), (size_hold, size_hold*6, size_hold*2, size_hold))


			screen.blit(text_7,(245,60))
			screen.blit(text_8,(755,60))
			screen.blit(text_9,(10*size_hold + 10, 9*size_hold + 30))
			screen.blit(text_12, (8*size_hold + 21, 8 * size_hold))
			screen.blit(text_13, (13*size_hold + 15, 8 * size_hold))

			now = datetime.now()
			current_time = now.strftime("%H : %M : %S ")
			text_current_time = font_time.render(str(current_time),True,BLACK)
			screen.blit(text_current_time, (size_hold, 9.5 * size_hold + 20))
			
			today = date.today()
			current_day = today.strftime("%B %d, %Y")
			text_current_day = font_time.render(str(current_day), True, BLACK)
			screen.blit(text_current_day, (size_hold, 10.5 * size_hold))

		pygame.draw.ellipse(screen, WHITE, (19.25*size_hold, 9.5*size_hold, size_hold*1.5, size_hold))
		screen.blit(text_10, (19.6*size_hold, 9.5*size_hold + 5))
		
		string_set_point = "set: " + str(set_point) + " points" 
		print_set_point = font_name.render(string_set_point,True, BLACK)
		screen.blit(print_set_point,(size_hold * 9 + 35, size_hold * 8 + 1))

		if channel_0.get_busy() == False:
			if sound_game == False:
				channel_0.play(sound_open_game)
			else:
		 		pygame.draw.line(screen,RED,(19.5*size_hold + (0.75/2)*size_hold, 10.5*size_hold), (20.5*size_hold - (0.75/2)*size_hold, 9.5*size_hold))

		for event in pygame.event.get():
			# đóng cửa sổ chương trình
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if start_game:
						if(size_hold*8 < mouse_x < size_hold*9 - 1) and (size_hold*8 + 1 < mouse_y < size_hold*9) and setUp:
							if not sound_game:
								channel_2.play(sound_modification)
							if set_point <= 0:
								set_point = 0
							else:
								set_point -= 1
						elif(size_hold*13 + 1 < mouse_x < size_hold*17) and (size_hold*8 + 1 < mouse_y < size_hold*9) and setUp:
							if not sound_game:
								channel_2.play(sound_modification)
							set_point += 1

						elif(size_hold*9 < mouse_x < size_hold*13) and (size_hold*9 < mouse_y < size_hold*11):
							if not sound_game:
								channel_2.play(sound_click)
							your_score, computer_score, player, draw_img_choose, setUp, result = reset(your_score, computer_score, player, draw_img_choose, setUp, result)
						
						elif set_point != 0:
							if (size_hold < mouse_x < size_hold*3) and (size_hold*3 < mouse_y < size_hold*4):
								if not sound_game:
									channel_2.play(sound_click)
								start = True
								setUp = False
								player = "Scissors"

							elif(size_hold < mouse_x < size_hold*3) and (size_hold*4.5 < mouse_y < size_hold*5.5):
								if not sound_game:
									channel_2.play(sound_click)
								start = True
								setUp = False
								player = "Rock"

							elif(size_hold < mouse_x < size_hold*3) and (size_hold*6 < mouse_y < size_hold*7):
								if not sound_game:
									channel_2.play(sound_click)
								start = True
								setUp = False
								player = "Paper"

					else:
						if (375 < mouse_x < 525) and (400 < mouse_y < 450):
							if not sound_game:
								channel_2.play(sound_click)
							start_game = True
							your_score, computer_score, player, draw_img_choose, setUp, result = reset(your_score, computer_score, player, draw_img_choose, setUp, result)

						elif (575 < mouse_x < 725) and (400 < mouse_y < 450):
							if not sound_game:
								channel_2.play(sound_click)
							running = False

					if(size_hold*19.25 < mouse_x < size_hold*20.75) and (size_hold*9.5 < mouse_y < size_hold*10.5):
						if channel_0.get_busy():
							pygame.mixer.stop()
							sound_game = True
						else:
							sound_game = False
		
		

		if start:
			random = randint(1,3)
			if random == 1:
				computer = "Scissors"
			if random == 2:
				computer = "Rock"
			if random == 3:
				computer = "Paper"

			if player == "Scissors":
				img_player_result = keo_img
			elif player == "Rock":
				img_player_result = bua_img
			else:
				img_player_result = Paper_img

			if computer == "Scissors":
				img_computer_result = keo_img
			elif computer == "Rock":
				img_computer_result = bua_img
			else :
				img_computer_result = Paper_img

			if player == computer:
				result = "DAW"

			elif player == "Scissors":
				if computer == "Rock":
					result = "COMPUTER WIN"
					if not sound_game:
						channel_1.play(sound_lose)
					computer_score += 1
				else:
					result = "YOU WIN"
					if not sound_game:
						channel_1.play(sound_win)
					your_score += 1
				  
			elif player == "Rock":
				if computer == "Paper":
					result = "COMPUTER WIN"
					if not sound_game:
						channel_1.play(sound_lose)
					computer_score += 1
				else:
					result = "YOU WIN"
					if not sound_game:
						channel_1.play(sound_win)
					your_score += 1
			elif player == "Paper":
				if computer == "Scissors":
					result = "COMPUTER WIN"

					if not sound_game:
						channel_1.play(sound_lose)
					computer_score += 1
				else:
					result = "YOU WIN"
					if not sound_game:
						channel_1.play(sound_win)
					your_score += 1
			
			if set_point == computer_score:
				if not sound_game:
					channel_1.play(sound_lose_game)
				start_game = False	
			elif set_point == your_score:
				if not sound_game:
					channel_1.play(sound_win_game)
				start_game = False	

			draw_img_choose = True
			start = False

		if not start_game:
			if computer_score > your_score:
				screen.blit(text_gameover,(350,150))
			else:
				screen.blit(text_victory,(400,150))


			pygame.draw.rect(screen, BLACK, (300,275,500,200))
			pygame.draw.rect(screen, ORANGE, (375,400,150,50))
			pygame.draw.rect(screen, RED_WHITE, (575,400,150,50))

			screen.blit(text_continue,(400,405))
			screen.blit(text_exit,(630,405))

			screen.blit(text_qestion_continue,(360, 300))

		else:
			your_score_text = str(your_score)
			computer_score_text = str(computer_score)

			your_result = font_text.render(your_score_text,True,BLACK)
			computer_result = font_text.render(computer_score_text,True,BLACK)
			screen.blit(your_result, (size_hold*7 - 10, size_hold*9.5))
			screen.blit(computer_result, (size_hold*15 - 10 , size_hold*9.5))

			if player == "" and set_point > 0 :
				result = "please make a choice"
			elif set_point == 0:
				result = "set point please"
				
			if draw_img_choose:
				screen.blit( pygame.transform.scale(img_player_result, (width_img_choose, height_img_choose)), (3.5*size_hold , 3.5*size_hold))
				screen.blit(pygame.transform.scale(img_computer_result, (width_img_choose, height_img_choose)),(14.5*size_hold , 3.5*size_hold ))

			text_11 = font_text.render(result,True,BLACK)
			text_14 = font_38.render(result,True,BLACK)

			if result == "COMPUTER WIN":
				screen.blit(text_11, (size_hold*8 + 20, size_hold*4 - 5))
				
			elif result == "YOU WIN":
				screen.blit(text_11, (size_hold*8 + 75, size_hold*4 - 5))
				
			elif result == "DAW":
				screen.blit(text_11, (size_hold*8 + 105, size_hold*4 -5))
			elif result == "set point please":
				screen.blit(text_11, (size_hold*8 + 35, size_hold*4 -5))
			else:
				screen.blit(text_14, (size_hold*8 , size_hold*4 -5))
				
		# vẻ lên màn hình
		pygame.display.flip()
	# xóa dữ liệu
	pygame.quit()
except Exception as bug:
	print(bug)