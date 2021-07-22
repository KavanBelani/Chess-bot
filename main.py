
import cordinates
cordinates.assignValues()

move=0
import os
os.system("clear")
import Queen
import Bestmove
# Bestmove.test()
import turtle
pen=turtle.Turtle()
#creates turtle called pen
turtle.tracer(0,0)
#allows turtle to draw faster
turtle.width(2)
import Pawn
import Legalm
import Characters
import rook
import SPAWN
import Oldpawn
import Open
import time
import knight
import Bishopm
import Pawn
import cordinates
import king
import LMFPGC



cords = cordinates.getValues()
wpa=cords[0]
wpb=cords[1]
wpc=cords[2]
wpd=cords[3]
wpe=cords[4]
wpf=cords[5]
wpg=cords[6]
wph=cords[7]
wra=cords[16]
wnb=cords[26]
wbc=cords[28]
wq=cords[20]
wk=cords[22]
wbf=cords[29]
wng=cords[27]
wrh=cords[17]
bpa=cords[8]
bpb=cords[9]
bpc=cords[10]
bpd=cords[11]
bpe=cords[12]
bpf=cords[13]
bpg=cords[14]
bph=cords[15]
bra=cords[18]
bnb=cords[25]
bbc=cords[30]
bq=cords[21]
bk=cords[23]
bbf=cords[31]
bng=cords[24]
brh=cords[19]
SPAWN.draw(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
SPAWN.draw(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#print(cordinates.whatPiece(1, 1))




# def usermove():

#   while True:
#   	start = input("\nEnter the cordinates of the piece you're moving \n > ")
#   	if len(start) != 3:
#   		print("\nUse the right format!")
#   		continue
#   	startx = start[0]
#   	starty = start[2]
#   	try:
#   		startx = int(startx)
#   	except:
#   		print("\nUse the right format!")
#   		continue
#   	try:
#   		starty = int(starty)
#   	except:
#   		print("\nUse the right format!")
#   		continue
#   	if startx > 8 or startx < 0:
#   		print("\nUse the right format!")
#   		continue
#   	if starty > 8 or starty < 0:
#   		print("\nUse the right format!")
#   		continue
#   	if Open.isblockedw(startx,starty,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)==False:
#   		print("\nYou dont have a piece there!")
#   		continue
#   	break
#   while True:
#   	piece=cordinates.whatPiece(startx, starty)
#   	if piece[1]=="p":
#   	  end = input("\nWhere would you like to move your pawn? \n > ")
#   	if piece[1]=="r":
#   	  end = input("\nWhere would you like to move your rook? \n > ")
#   	if piece[1]=="n":
#   	  end = input("\nWhere would you like to move your knight? \n > ")
#   	if piece[1]=="b":
#   	  end = input("\nWhere would you like to move your bishop? \n > ")
#   	if piece[1]=="q":
#   	  end = input("\nWhere would you like to move your queen? \n > ")
#   	if piece[1]=="k":
#   	  end = input("\nWhere would you like to move your king? \n > ")
#   	if len(end) != 3:
#   		print("\nUse the right format!")
#   		continue
#   	endx = end[0]
#   	endy = end[2]
#   	try:
#   		endx = int(endx)
#   	except:
#   		print("\nUse the right format!")
#   		continue
#   	try:
#   		endy = int(endy)
#   	except:
#   		print("\nUse the right format!")
#   		continue
#   	if endx > 8 or endx < 0:
#   		print("\nUse the right format!")
#   		continue
#   	if endy > 8 or endy < 0:
#   		print("\nUse the right format!")
#   		continue
#   	if (endx == startx) and (endy == starty):
#   		print("\nYou need to move!")
#   		continue
#   	if Open.isblockedw(endx,endy,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh) == True:
#   		print("\nThat place is blocked!")
#   		continue
  	
  	
#   	#Put any other input validation above this
#   	legalmovesfp = LMFPGC.LMFPGC(startx,starty)
#   	endCord = (endx, endy)
  	
#   	legal = False
#   	for i in range(len(legalmovesfp)):
  		
#   		if endCord == legalmovesfp[i]:
#   			legal = True
#   			break
#   	if legal == False:
#   		print("\nNot a legal move")
#   		continue
#   	else:
#   		break
  	
  	
  	
  	
  	
  	
#   print("\nCleared!")
  
  
#   piece = cordinates.whatPiece(startx, starty)
#   cor = (endx, endy)
#   if piece == "wpa":
#     cordinates.changeValues(cor,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "wpb":
#     cordinates.changeValues(wpa,cor,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "wpc":
#   	cordinates.changeValues(wpa,wpb,cor,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "wpd":
#   	cordinates.changeValues(wpa,wpb,wpc,cor,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "wpe":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,cor,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "wpf":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,cor,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "wpg":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,cor,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "wph":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,cor,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  
#   elif piece == "bpa":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,cor,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "bpb":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,cor,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "bpc":
#     cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,cor,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "bpd":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,cor,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "bpe":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,cor,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "bpf":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,cor,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "bpg":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,cor,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "bph":
#     cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,cor,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	
#   elif piece == "bra":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,cor,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "bnb":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,cor,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "bbc":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,cor,bbf)
#   elif piece == "bq":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,cor,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "bk":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,cor,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "bbf":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,cor)
#   elif piece == "bng":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,cor,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "brh":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,cor,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	
#   elif piece == "wra":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,cor,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "wnb":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,cor,wng,wbc,wbf,bbc,bbf)
#   elif piece == "wbc":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,cor,wbf,bbc,bbf)
#   elif piece == "wq":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,cor,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "wk":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,cor,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   elif piece == "wbf":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,cor,bbc,bbf)
#   elif piece == "wng":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,cor,wbc,wbf,bbc,bbf)
#   elif piece == "wrh":
#   	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,cor,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   # SPAWN.draw(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  
  
# while True:  
#   usermove()
  
  
  
  	
  	
  	
#   print(cordinates.getValues())
#   blackmoves=Legalm.black_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   whitemoves=Legalm.white_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
#   print("Black moves:",str(blackmoves))
#   print("White moves:",str(whitemoves))
    
while True:  
  cordinates.usermove()
  
  
  
  	
  	
  	
  cords = cordinates.getValues()
  wpa=cords[0]
  wpb=cords[1]
  wpc=cords[2]
  wpd=cords[3]
  wpe=cords[4]
  wpf=cords[5]
  wpg=cords[6]
  wph=cords[7]
  wra=cords[16]
  wnb=cords[26]
  wbc=cords[28]
  wq=cords[20]
  wk=cords[22]
  wbf=cords[29]
  wng=cords[27]
  wrh=cords[17]
  bpa=cords[8]
  bpb=cords[9]
  bpc=cords[10]
  bpd=cords[11]
  bpe=cords[12]
  bpf=cords[13]
  bpg=cords[14]
  bph=cords[15]
  bra=cords[18]
  bnb=cords[25]
  bbc=cords[30]
  bq=cords[21]
  bk=cords[23]
  bbf=cords[31]
  bng=cords[24]
  brh=cords[19]
  
  # print("Black moves:",str(blackmoves))
  # print("White moves:",str(whitemoves))
  cordinates.changeValuest(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  blackmoves=Legalm.black_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  whitemoves=Legalm.white_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  botmove=Bestmove.best(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  piece = botmove[1]
  cor =botmove[2]
  if piece == "bpa":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,cor,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bpb":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,cor,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bpc":
    cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,cor,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bpd":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,cor,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bpe":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,cor,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bpf":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,cor,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bpg":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,cor,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bph":
    cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,cor,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	
  elif piece == "bra":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,cor,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bnb":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,cor,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bbc":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,cor,bbf)
  elif piece == "bq":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,cor,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bk":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,cor,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bbf":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,cor)
  elif piece == "bng":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,cor,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "brh":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,cor,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	
  elif piece == "wra":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,cor,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "wnb":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,cor,wng,wbc,wbf,bbc,bbf)
  elif piece == "wbc":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,cor,wbf,bbc,bbf)
  elif piece == "wq":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,cor,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "wk":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,cor,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "wbf":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,cor,bbc,bbf)
  elif piece == "wng":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,cor,wbc,wbf,bbc,bbf)
  elif piece == "wrh":
  	cordinates.changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,cor,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  
  	
  	
  cords = cordinates.getValues()
  wpa=cords[0]
  wpb=cords[1]
  wpc=cords[2]
  wpd=cords[3]
  wpe=cords[4]
  wpf=cords[5]
  wpg=cords[6]
  wph=cords[7]
  wra=cords[16]
  wnb=cords[26]
  wbc=cords[28]
  wq=cords[20]
  wk=cords[22]
  wbf=cords[29]
  wng=cords[27]
  wrh=cords[17]
  bpa=cords[8]
  bpb=cords[9]
  bpc=cords[10]
  bpd=cords[11]
  bpe=cords[12]
  bpf=cords[13]
  bpg=cords[14]
  bph=cords[15]
  bra=cords[18]
  bnb=cords[25]
  bbc=cords[30]
  bq=cords[21]
  bk=cords[23]
  bbf=cords[31]
  bng=cords[24]
  brh=cords[19]
  
  # print("Black moves:",str(blackmoves))
  # print("White moves:",str(whitemoves))
  cordinates.changeValuest(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  blackmoves=Legalm.black_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  whitemoves=Legalm.white_moves(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  SPAWN.draw(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
    
  


  SPAWN.draw(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)