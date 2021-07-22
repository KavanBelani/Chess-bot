
import SPAWN
import Open


def assignValues():
	global wpa
	global wpb
	global wpc
	global wpd
	global wpe
	global wpf
	global wpg
	global wph
	global bpa
	global bpb
	global bpc
	global bpd
	global bpe
	global bpf
	global bpg
	global bph
	global wra
	global wnb
	global wbc
	global wq
	global wk
	global wbf
	global wng
	global wrh
	global bra
	global bnb
	global bbc
	global bq
	global bk
	global bbf
	global bng
	global brh
	
	wpa=(1,2)
	wpb=(2,2)
	wpc=(3,2)
	wpd=(4,2)
	wpe=(5,2)
	wpf=(6,2)
	wpg=(7,2)
	wph=(8,2)
	wra=(1,1)
	wnb=(2,1)
	wbc=(3,1)
	wq=(4,1)
	wk=(5,1)
	wbf=(6,1)
	wng=(7,1)
	wrh=(8,1)
	bpa=(1,7)
	bpb=(2,7)
	bpc=(3,7)
	bpd=(4,7)
	bpe=(5,7)
	bpf=(6,7)
	bpg=(7,7)
	bph=(8,7)
	bra=(1,8)
	bnb=(2,8)
	bbc=(3,8)
	bq=(4,8)
	bk=(5,8)
	bbf=(6,8)
	bng=(7,8)
	brh=(8,8)
	





#THESE ARE TWO VERY HELPFUL FUNCTIONS
#USE THEM: -Jack


def getValues():
	return(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)





def changeValues(wpa1,wpb1,wpc1,wpd1,wpe1,wpf1,wpg1,wph1,bpa1,bpb1,bpc1,bpd1,bpe1,bpf1,bpg1,bph1,wra1,wrh1,bra1,brh1,wq1,bq1,wk1,bk1,bng1,bnb1,wnb1,wng1,bcc,wbf1,bbc1,bbf1):
  global wpa
  global wpb
  global wpc
  global wpd
  global wpe
  global wpf
  global wpg
  global wph
  global bpa
  global bpb
  global bpc
  global bpd
  global bpe
  global bpf
  global bpg
  global bph
  global wra
  global wnb
  global wbc
  global wq
  global wk
  global wbf
  global wng
  global wrh
  global bra
  global bnb
  global bbc
  global bq
  global bk
  global bbf
  global bng
  global brh
  wpa = wpa1
  wpb = wpb1
  wpc = wpc1
  wpd = wpd1
  wpe = wpe1
  wpf = wpf1
  wpg = wpg1
  wph = wph1
  bpa = bpa1
  bpb = bpb1
  bpc = bpc1
  bpd = bpd1
  bpe = bpe1
  bpf = bpf1
  bpg = bpg1
  bph = bph1
  wra = wra1
  bq = bq1
  wrh = wrh1
  bra = bra1
  brh = brh1
  wq = wq1
  wk = wk1
  bk = bk1
  bng = bng1
  bnb = bnb1
  wnb = wnb1
  wng = wng1
  wbf = wbf1
  bbc = bbc1
  bbf = bbf1
  
  SPAWN.draw(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)

def changeValuest(wpa1,wpb1,wpc1,wpd1,wpe1,wpf1,wpg1,wph1,bpa1,bpb1,bpc1,bpd1,bpe1,bpf1,bpg1,bph1,wra1,wrh1,bra1,brh1,wq1,bq1,wk1,bk1,bng1,bnb1,wnb1,wng1,bcc,wbf1,bbc1,bbf1):
  global wpa
  global wpb
  global wpc
  global wpd
  global wpe
  global wpf
  global wpg
  global wph
  global bpa
  global bpb
  global bpc
  global bpd
  global bpe
  global bpf
  global bpg
  global bph
  global wra
  global wnb
  global wbc
  global wq
  global wk
  global wbf
  global wng
  global wrh
  global bra
  global bnb
  global bbc
  global bq
  global bk
  global bbf
  global bng
  global brh
	
  wpa = wpa1
  wpb = wpb1
  wpc = wpc1
  wpd = wpd1
  wpe = wpe1
  wpf = wpf1
  wpg = wpg1
  wph = wph1
  bpa = bpa1
  bpb = bpb1
  bpc = bpc1
  bpd = bpd1
  bpe = bpe1
  bpf = bpf1
  bpg = bpg1
  bph = bph1
  wra = wra1
  bq = bq1
  wrh = wrh1
  bra = bra1
  brh = brh1
  wq = wq1
  wk = wk1
  bk = bk1
  bng = bng1
  bnb = bnb1
  wnb = wnb1
  wng = wng1
  wbf = wbf1
  bbc = bbc1
  bbf = bbf1
  
def whatPiece(x,y):
	cor = (x,y)
	if cor == wpa:
		return("wpa")
	elif cor == wpb:
		return("wpb")
	elif cor == wpc:
		return("wpc")
	elif cor == wpd:
		return("wpd")
	elif cor == wpe:
		return("wpe")
	elif cor == wpf:
		return("wpf")
	elif cor == wpg:
		return("wpg")
	elif cor == wph:
		return("wph")
	
	elif cor == bpa:
		return("bpa")
	elif cor == bpb:
		return("bpb")
	elif cor == bpc:
		return("bpc")
	elif cor == bpd:
		return("bpd")
	elif cor == bpe:
		return("bpe")
	elif cor == bpf:
		return("bpf")
	elif cor == bpg:
		return("bpg")
	elif cor == bph:
		return("bph")
	
	elif cor == bra:
		return("bra")
	elif cor == bnb:
		return("bnb")
	elif cor == bbc:
		return("bbc")
	elif cor == bq:
		return("bq")
	elif cor == bk:
		return("bk")
	elif cor == bbf:
		return("bbf")
	elif cor == bng:
		return("bng")
	elif cor == brh:
		return("brh")

	elif cor == wra:
		return("wra")
	elif cor == wnb:
		return("wnb")
	elif cor ==wbc:
		return("wbc")
	elif cor == wq:
		return("wq")
	elif cor == wk:
		return("wk")
	elif cor == wbf:
		return("wbf")
	elif cor == wng:
		return("wng")
	elif cor == wrh:
		return("wrh")
	else:
		return("none")



def usermove():

  while True:
  	start = input("\nEnter the cordinates of the piece you're moving \n > ")
  	if len(start) != 3:
  		print("\nUse the right format!")
  		continue
  	startx = start[0]
  	starty = start[2]
  	try:
  		startx = int(startx)
  	except:
  		print("\nUse the right format!")
  		continue
  	try:
  		starty = int(starty)
  	except:
  		print("\nUse the right format!")
  		continue
  	if startx > 8 or startx < 0:
  		print("\nUse the right format!")
  		continue
  	if starty > 8 or starty < 0:
  		print("\nUse the right format!")
  		continue
  	if Open.isblockedw(startx,starty,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh)==False:
  		print("\nYou dont have a piece there!")
  		continue
  	break
  while True:
  	piece=whatPiece(startx, starty)
  	if piece[1]=="p":
  	  end = input("\nWhere would you like to move your pawn? \n > ")
  	if piece[1]=="r":
  	  end = input("\nWhere would you like to move your rook? \n > ")
  	if piece[1]=="n":
  	  end = input("\nWhere would you like to move your knight? \n > ")
  	if piece[1]=="b":
  	  end = input("\nWhere would you like to move your bishop? \n > ")
  	if piece[1]=="q":
  	  end = input("\nWhere would you like to move your queen? \n > ")
  	if piece[1]=="k":
  	  end = input("\nWhere would you like to move your king? \n > ")
  	if len(end) != 3:
  		print("\nUse the right format!")
  		continue
  	if end == 'nvm':
  		userMove()
  	endx = end[0]
  	endy = end[2]
  	try:
  		endx = int(endx)
  	except:
  		print("\nUse the right format!")
  		continue
  	try:
  		endy = int(endy)
  	except:
  		print("\nUse the right format!")
  		continue
  	if endx > 8 or endx < 0:
  		print("\nUse the right format!")
  		continue
  	if endy > 8 or endy < 0:
  		print("\nUse the right format!")
  		continue
  	if (endx == startx) and (endy == starty):
  		print("\nYou need to move!")
  		continue
  	if Open.isblockedw(endx,endy,wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,wra,wnb,wbc,wq,wk,wbf,wng,wrh) == True:
  		print("\nThat place is blocked!")
  		continue
  	
  	
  	#Put any other input validation above 
  	import LMFPGC
  	legalmovesfp = LMFPGC.LMFPGC(startx,starty)
  	endCord = (endx,endy)
  	
  	legal = False
  	for i in range(len(legalmovesfp)):
  		
  		if endCord == legalmovesfp[i]:
  			legal = True
  			break
  	if legal == False:
  		print("\nNot a legal move")
  		continue
  	else:
  		break
  print("\nCleared!")
  piece = whatPiece(startx,starty)
  cor = (endx,endy)
  if piece == "wpa":
    changeValuest(cor,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "wpb":
    changeValues(wpa,cor,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "wpc":
  	changeValues(wpa,wpb,cor,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "wpd":
  	changeValues(wpa,wpb,wpc,cor,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "wpe":
  	changeValues(wpa,wpb,wpc,wpd,cor,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "wpf":
  	changeValues(wpa,wpb,wpc,wpd,wpe,cor,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "wpg":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,cor,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "wph":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,cor,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  
  elif piece == "bpa":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,cor,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bpb":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,cor,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bpc":
    changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,cor,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bpd":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,cor,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bpe":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,cor,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bpf":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,cor,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bpg":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,cor,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bph":
    changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,cor,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	
  elif piece == "bra":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,cor,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bnb":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,cor,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bbc":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,cor,bbf)
  elif piece == "bq":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,cor,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bk":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,cor,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "bbf":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,cor)
  elif piece == "bng":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,cor,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "brh":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,cor,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
	
  elif piece == "wra":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,cor,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "wnb":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,cor,wng,wbc,wbf,bbc,bbf)
  elif piece == "wbc":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,cor,wbf,bbc,bbf)
  elif piece == "wq":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,cor,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "wk":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,cor,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  elif piece == "wbf":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,cor,bbc,bbf)
  elif piece == "wng":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,cor,wbc,wbf,bbc,bbf)
  elif piece == "wrh":
  	changeValues(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,cor,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
  # SPAWN.draw(wpa,wpb,wpc,wpd,wpe,wpf,wpg,wph,bpa,bpb,bpc,bpd,bpe,bpf,bpg,bph,wra,wrh,bra,brh,wq,bq,wk,bk,bng,bnb,wnb,wng,wbc,wbf,bbc,bbf)
    
  

